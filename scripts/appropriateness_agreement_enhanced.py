"""
Enhanced Appropriateness Agreement Analysis Script

Computes inter-rater agreement statistics for crisis appropriateness scores (1-5 Likert scale)
with weighted Cohen's kappa, bias metrics, and LLM self-consistency diagnostics.

USAGE:
    python scripts/appropriateness_agreement_enhanced.py [--aggregation-method median|mean_round_half_up]

OPTIONS:
    --sampled_path PATH             Path to sampled dataset JSON (default: data/llm_evaluator/sampled/sampled_lowest_scores_n200.json)
    --evaluator-paths NAME=PATH ... LLM evaluator paths as 'name=path' pairs (auto-detected from data/llm_evaluator/*/n_200/merged if not provided)
    --human_score_paths PATH ...    Human score XLSX files (auto-detected from data/human_label/*_scores_n206_s42.xlsx if not provided)
    --output_dir DIR                Output directory (default: outputs/appropriateness_agreement_enhanced)
    --min_rating INT                Minimum rating value (default: 1)
    --max_rating INT                Maximum rating value (default: 5)
    --aggregation_method STR        LLM aggregation: 'median' (default) or 'mean_round_half_up'

OUTPUTS:
    outputs/appropriateness_agreement_enhanced/appropriateness_agreement_enhanced_report.md
        - Aggregation protocol
        - Pairwise MAE, RMSE, Within-1, Quadratic Weighted Kappa, Signed Error matrices
        - LLM Average Agreement with Humans (extended with κ_w and bias)
        - Human-Human Agreement
        - LLM Self-Consistency (intra-LLM MAE, κ_w, range variability)
        - Confusion matrix summaries per LLM
        - Full confusion matrices (mean scores and raw evals)
    
    outputs/appropriateness_agreement_enhanced/pairwise_*.csv
        - MAE, RMSE, Within-1, Kappa, Signed Error matrices

METRICS:
    - MAE: Mean Absolute Error on 1-5 scale (lower is better)
    - RMSE: Root Mean Square Error (lower is better)
    - Within-1: % of pairs within ±1 point (higher is better)
    - Quadratic Weighted Kappa: Ordinal agreement (higher is better, range -inf to 1)
    - Signed Error: Bias (positive = over-rate, negative = under-rate)
    - Confusion Matrices: Rounded to nearest integer using half-up rounding
"""

import argparse
import ast
import glob
import json
import math
import os
import statistics
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def normalize_text(text: str) -> str:
    if text is None:
        return ""
    return str(text).replace("\r\n", "\n").strip()


def normalize_inputs(inputs) -> List[str]:
    if isinstance(inputs, list):
        return [normalize_text(x) for x in inputs]
    if isinstance(inputs, str):
        return [normalize_text(inputs)]
    return [normalize_text(str(inputs))]


def make_key(inputs, answer: str) -> str:
    norm_inputs = normalize_inputs(inputs)
    norm_answer = normalize_text(answer)
    return json.dumps(norm_inputs, ensure_ascii=False) + "||" + norm_answer


def round_half_up(value: float) -> int:
    return int(math.floor(value + 0.5))


def to_likert(value: float, min_rating: int, max_rating: int) -> int:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    try:
        v = float(value)
    except (TypeError, ValueError):
        return None
    v = round_half_up(v)
    return max(min_rating, min(max_rating, v))


def is_valid_score(value) -> bool:
    if value is None:
        return False
    if isinstance(value, float) and math.isnan(value):
        return False
    return True


def parse_evaluator_arg(arg: str) -> Tuple[str, str]:
    if "=" in arg:
        name, path = arg.split("=", 1)
        return name.strip(), path.strip()
    path = arg.strip()
    parent = os.path.basename(os.path.dirname(os.path.dirname(path)))
    name = parent if parent else os.path.basename(path)
    return name, path


def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_human_scores_xlsx(path: str) -> List[float]:
    """Load human scores from XLSX, returning list of scores (in order, with NaN for missing)."""
    df = pd.read_excel(path, engine="openpyxl")
    df.columns = [str(c).strip() for c in df.columns]
    cols_lower = {c: c.lower().strip() for c in df.columns}

    score_col = None
    for c, lc in cols_lower.items():
        if lc == "evaluation":
            score_col = c
            break

    if score_col is None:
        raise ValueError(
            f"Missing required column 'evaluation' in {path}. Found columns: {list(df.columns)}"
        )

    return df[score_col].tolist()


def load_human_scores_json(path: str) -> List[float]:
    """Load human scores from JSON, returning list of scores in order."""
    data = load_json(path)
    if isinstance(data, list):
        if data and isinstance(data[0], dict):
            if "evaluation" not in data[0]:
                raise ValueError(f"Missing 'evaluation' field in {path}")
            return [item.get("evaluation") for item in data]
        return data
    raise ValueError(f"Unexpected JSON format in {path}")


def normalize_human_rater_name(filename: str) -> str:
    base = os.path.splitext(os.path.basename(filename))[0]
    if base.startswith("H1_"):
        return "H1"
    if base.startswith("H2_"):
        return "H2"
    return base


def build_evaluator_score_map(merged_dir: str) -> Dict[str, Tuple[float, str]]:
    merged_files = sorted(glob.glob(os.path.join(merged_dir, "*.json")))
    score_map = {}
    for file_path in merged_files:
        data = load_json(file_path)
        for item in data:
            key = make_key(item.get("inputs"), item.get("answer"))
            eval_score = item.get("evaluation", None)
            if key in score_map:
                prev_score, prev_file = score_map[key]
                if prev_score != eval_score:
                    pass  # Keep first, silent
                continue
            score_map[key] = (eval_score, os.path.basename(file_path))
    return score_map


def aligned_scores(sampled: List[dict], score_map: Dict[str, float]) -> List[float]:
    scores = []
    for item in sampled:
        key = make_key(item.get("inputs"), item.get("answer"))
        scores.append(score_map.get(key))
    return scores


def ensure_dir(path: str) -> None:
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


# ============================================================================
# AGGREGATION FUNCTIONS
# ============================================================================

def aggregate_llm_scores(scores_3: List[float], method: str = "mean") -> float:
    """
    Aggregate 3 LLM evaluation scores.
    
    Args:
        scores_3: List of exactly 3 float scores
        method: 'mean' (default) or 'median'
    
    Returns:
        Aggregated score as float
    """
    valid_scores = [s for s in scores_3 if is_valid_score(s)]
    
    if not valid_scores:
        return None
    
    if method == "mean":
        return statistics.mean(valid_scores)
    elif method == "median":
        return statistics.median(valid_scores)
    else:
        raise ValueError(f"Unknown aggregation method: {method}")


def mean_signed_error(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """
    Compute mean signed error (bias): mean(y_pred - y_true).
    
    Positive = over-rate (predict higher than true).
    Negative = under-rate (predict lower than true).
    """
    return np.mean(y_pred - y_true)


# ============================================================================
# WEIGHTED COHEN'S KAPPA (QUADRATIC WEIGHTS)
# ============================================================================

def weighted_cohen_kappa_quadratic(y_a: np.ndarray, y_b: np.ndarray, K: int = 5) -> float:
    """
    Compute weighted Cohen's kappa with quadratic weights.
    
    Used for ordinal data. Penalizes large disagreements more heavily.
    
    Args:
        y_a, y_b: Integer arrays in {1..K}, same length
        K: Number of ordinal categories (default 5)
    
    Returns:
        Weighted kappa value (range -∞ to 1, where 1 = perfect agreement)
    """
    # Remove NaN/None pairs
    mask = ~(pd.isna(y_a) | pd.isna(y_b))
    y_a = y_a[mask]
    y_b = y_b[mask]
    
    if len(y_a) == 0:
        return np.nan
    
    # Shift to 0-indexed for easier array indexing
    y_a = np.array(y_a, dtype=int) - 1
    y_b = np.array(y_b, dtype=int) - 1
    
    # Build confusion matrix (0-indexed)
    n_ij = confusion_matrix(y_a, y_b, labels=list(range(K)))
    n = n_ij.sum()
    
    if n == 0:
        return np.nan
    
    # Proportions
    p_ij = n_ij / n
    p_i = p_ij.sum(axis=1)  # row marginals
    p_j = p_ij.sum(axis=0)  # col marginals
    
    # Quadratic weights: w_ij = 1 - ((i-j)/(K-1))**2
    w = np.zeros((K, K))
    for i in range(K):
        for j in range(K):
            w[i, j] = 1.0 - ((i - j) / (K - 1)) ** 2
    
    # Observed agreement
    p_o = np.sum(w * p_ij)
    
    # Expected agreement
    p_e = 0.0
    for i in range(K):
        for j in range(K):
            p_e += w[i, j] * p_i[i] * p_j[j]
    
    # Kappa
    if abs(1.0 - p_e) < 1e-10:
        return np.nan
    
    kappa = (p_o - p_e) / (1.0 - p_e)
    return kappa


# ============================================================================
# SELF-CONSISTENCY DIAGNOSTICS
# ============================================================================

def compute_intra_llm_consistency(
    sampled: List[dict],
    merged_dir: str,
    min_rating: int = 1,
    max_rating: int = 5
) -> Dict[str, float]:
    """
    Compute LLM self-consistency metrics across 3 runs.
    
    Returns dict with:
        - intra_llm_mae: Average MAE between run pairs
        - intra_llm_kappa_w: Average quadratic weighted kappa between run pairs
        - range_ge_2_rate: Fraction of items where max(run)-min(run) >= 2
    """
    # Load raw evaluations from merged files
    merged_files = sorted(glob.glob(os.path.join(merged_dir, "*.json")))
    
    # Map key -> list of evals
    key_to_evals = {}
    sampled_keys = {make_key(item.get("inputs"), item.get("answer")): item for item in sampled}
    
    for merged_file in merged_files:
        try:
            with open(merged_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        key = make_key(item.get("inputs"), item.get("answer"))
                        if key in sampled_keys:
                            evals = item.get("evals", [])
                            if evals:
                                key_to_evals[key] = evals
        except Exception:
            pass
    
    # Collect run pairs
    run_pairs_mae = []
    run_pairs_kappa = []
    range_ge_2_counts = 0
    valid_items = 0
    
    for key in sampled_keys:
        if key in key_to_evals:
            evals = key_to_evals[key]
            if len(evals) >= 3:
                evals = evals[:3]  # Take first 3
                # Convert to Likert
                evals_likert = [to_likert(e, min_rating, max_rating) for e in evals]
                evals_likert = [e for e in evals_likert if e is not None]
                
                if len(evals_likert) >= 2:
                    valid_items += 1
                    
                    # Check range >= 2
                    if max(evals_likert) - min(evals_likert) >= 2:
                        range_ge_2_counts += 1
                    
                    # Pairwise MAE and kappa
                    for i in range(len(evals_likert)):
                        for j in range(i + 1, len(evals_likert)):
                            mae = abs(evals_likert[i] - evals_likert[j])
                            run_pairs_mae.append(mae)
                            # Kappa for single pair (0 or 1)
                            if evals_likert[i] == evals_likert[j]:
                                kappa_val = 1.0
                            else:
                                # Use two-point data
                                y_a = np.array([evals_likert[i]], dtype=int)
                                y_b = np.array([evals_likert[j]], dtype=int)
                                kappa_val = weighted_cohen_kappa_quadratic(y_a, y_b, K=5)
                                if np.isnan(kappa_val):
                                    kappa_val = 0.0
                            run_pairs_kappa.append(kappa_val)
    
    result = {
        "intra_llm_mae": np.mean(run_pairs_mae) if run_pairs_mae else np.nan,
        "intra_llm_kappa_w": np.mean(run_pairs_kappa) if run_pairs_kappa else np.nan,
        "range_ge_2_rate": (range_ge_2_counts / valid_items * 100) if valid_items > 0 else np.nan,
    }
    return result


# ============================================================================
# CONFUSION MATRIX SUMMARIES
# ============================================================================

def confusion_matrix_summary(y_true: List[int], y_pred: List[int], K: int = 5) -> Dict[str, float]:
    """
    Compute summary statistics from a confusion matrix.
    
    Returns:
        - exact_agreement_pct: % where y_true == y_pred
        - within_1_pct: % where |y_true - y_pred| <= 1
        - over_pct: % where y_pred > y_true
        - under_pct: % where y_pred < y_true
        - signed_error: mean(y_pred - y_true)
    """
    if not y_true or not y_pred:
        return {}
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    n = len(y_true)
    exact = np.sum(y_true == y_pred) / n * 100
    within_1 = np.sum(np.abs(y_true - y_pred) <= 1) / n * 100
    over = np.sum(y_pred > y_true) / n * 100
    under = np.sum(y_pred < y_true) / n * 100
    signed_err = np.mean(y_pred - y_true)
    
    return {
        "exact_agreement_pct": exact,
        "within_1_pct": within_1,
        "over_pct": over,
        "under_pct": under,
        "signed_error": signed_err,
    }


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enhanced inter-rater agreement analysis with Cohen's kappa and bias metrics."
    )
    parser.add_argument(
        "--sampled_path",
        type=str,
        default="data/llm_evaluator/sampled/sampled_lowest_scores_n200.json",
        help="Path to sampled dataset with lowest scores.",
    )
    parser.add_argument(
        "--human_score_paths",
        nargs="+",
        default=None,
        help="Paths to human score XLSX files (default: data/human_label/*_scores_n206_s42.xlsx).",
    )
    parser.add_argument(
        "--llm_evaluator_dirs",
        nargs="+",
        default=None,
        help=(
            "Merged evaluation dirs. Format: name=path or path. "
            "Example: gpt-5-nano=data/llm_evaluator/gpt-5-nano/n_200/merged"
        ),
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="outputs/appropriateness_agreement_enhanced",
        help="Output directory for reports.",
    )
    parser.add_argument(
        "--min_rating",
        type=int,
        default=1,
        help="Minimum likert rating.",
    )
    parser.add_argument(
        "--max_rating",
        type=int,
        default=5,
        help="Maximum likert rating.",
    )
    parser.add_argument(
        "--aggregation_method",
        type=str,
        default="mean",
        choices=["mean", "median"],
        help="LLM aggregation method for 3 runs (default: mean).",
    )
    args = parser.parse_args()

    sampled = load_json(args.sampled_path)
    print(f"Loaded sampled set: {len(sampled)} items")

    rater_scores: Dict[str, List[float]] = {}

    # gpt-4o-mini scores from sampled file (use raw, will aggregate later)
    gpt4o_raw_3 = [item.get("evaluation", None) for item in sampled]
    
    # LLM evaluator scores (raw, 3 per item)
    llm_raw_3: Dict[str, List[float]] = {}
    llm_dirs = args.llm_evaluator_dirs
    if llm_dirs is None:
        llm_dirs = [
            "gpt-5-nano=data/llm_evaluator/gpt-5-nano/n_200/merged",
            "meta-llama=data/llm_evaluator/meta-llama/n_200/merged",
        ]

    for entry in llm_dirs:
        name, path = parse_evaluator_arg(entry)
        score_map = build_evaluator_score_map(path)
        aligned = []
        for item in sampled:
            key = make_key(item.get("inputs"), item.get("answer"))
            if key in score_map:
                score, src = score_map[key]
                aligned.append(score)
            else:
                aligned.append(None)
        llm_raw_3[name] = aligned
        print(f"Loaded {name}: {sum(1 for s in aligned if is_valid_score(s))} scores")

    # Human scores
    human_paths = args.human_score_paths
    if human_paths is None:
        anonymized_json = [
            "data/human_label/H1_scores_n206_s42.json",
            "data/human_label/H2_scores_n206_s42.json",
        ]
        if all(os.path.exists(p) for p in anonymized_json):
            human_paths = anonymized_json
        else:
            human_paths = [
                p for p in glob.glob("data/human_label/*_scores_n206_s42.xlsx")
                if not os.path.basename(p).startswith("~$")
            ]

    for hp in human_paths:
        rater_name = normalize_human_rater_name(hp)
        if hp.lower().endswith(".json"):
            scores_list = load_human_scores_json(hp)
        else:
            scores_list = load_human_scores_xlsx(hp)
        if len(scores_list) != len(sampled):
            raise ValueError(
                f"Score count mismatch in {hp}: {len(scores_list)} rows vs {len(sampled)} expected"
            )
        rater_scores[rater_name] = scores_list

    # Aggregate LLM scores
    print(f"Aggregating LLM scores using method: {args.aggregation_method}")
    
    # gpt-4o-mini: single score per item
    rater_scores["gpt-4o-mini"] = gpt4o_raw_3
    
    # Other LLMs: use loaded aggregated scores
    for name in llm_raw_3:
        rater_scores[name] = llm_raw_3[name]

    # Setup for report
    raters = list(rater_scores.keys())
    llm_raters = ["gpt-4o-mini", "gpt-5-nano", "meta-llama"]
    human_raters = [r for r in raters if r not in llm_raters and r != "LLM-Jury"]
    
    # Create LLM Jury (mean of 3 LLMs)
    jury_scores = []
    for i in range(len(sampled)):
        llm_vals = [rater_scores[llm][i] for llm in llm_raters if llm in rater_scores]
        llm_vals = [v for v in llm_vals if is_valid_score(v)]
        if llm_vals:
            jury_scores.append(sum(llm_vals) / len(llm_vals))
        else:
            jury_scores.append(None)
    rater_scores["LLM-Jury"] = jury_scores
    
    # Save jury scores to JSON
    jury_path = "data/llm_evaluator/sampled/sampled_lowest_scores_n200__jury.json"
    ensure_dir(os.path.dirname(jury_path))
    jury_data = []
    for idx, item in enumerate(sampled):
        # Collect individual LLM evaluations
        llm_evals = {}
        for llm in llm_raters:
            if llm in rater_scores:
                llm_evals[llm] = rater_scores[llm][idx]
        
        jury_data.append({
            "inputs": item.get("inputs"),
            "answer": item.get("answer"),
            "label": item.get("label"),
            "dataset_id": item.get("dataset_id"),
            "evaluation": jury_scores[idx],
            "llm_evaluations": llm_evals,
            "source": "mean of gpt-4o-mini, gpt-5-nano, meta-llama"
        })
    with open(jury_path, "w", encoding="utf-8") as f:
        json.dump(jury_data, f, ensure_ascii=False, indent=2)
    print(f"Saved LLM-Jury scores: {jury_path}")
    
    # Update raters list
    raters = list(rater_scores.keys())

    # Pairwise matrices
    mae_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    rmse_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    within1_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    kappa_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    signed_error_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)

    report_lines = []
    report_lines.append("# Enhanced Appropriateness Agreement Report")
    
    # Aggregation protocol section
    report_lines.append("\n## Aggregation Protocol")
    report_lines.append(f"- LLM per-item aggregation: **{args.aggregation_method}** of 3 stochastic evaluations")
    report_lines.append("- Human scores: Individual rater scores (no consensus)")
    report_lines.append("- Pairwise agreement tables: Based on aggregated per-item scores (190 valid items)")
    report_lines.append("- Raw evaluation matrices: Unrolled 3-per-item evals (after filtering), separate section")

    report_lines.append("\n## Rater coverage")
    for r in raters:
        non_null = sum(1 for x in rater_scores[r] if is_valid_score(x))
        report_lines.append(f"- {r}: {non_null} scored / {len(sampled)}")

    # Compute pairwise matrices
    for i, ra in enumerate(raters):
        for j, rb in enumerate(raters):
            if i == j:
                mae_matrix.loc[ra, rb] = 0.0
                rmse_matrix.loc[ra, rb] = 0.0
                within1_matrix.loc[ra, rb] = 100.0
                kappa_matrix.loc[ra, rb] = 1.0
                signed_error_matrix.loc[ra, rb] = 0.0
                continue

            paired = [
                (a, b)
                for a, b in zip(rater_scores[ra], rater_scores[rb])
                if is_valid_score(a) and is_valid_score(b)
            ]

            if not paired:
                mae = np.nan
                rmse = np.nan
                within1 = np.nan
                kappa = np.nan
                signed_err = np.nan
            else:
                a_vals = np.array([p[0] for p in paired], dtype=float)
                b_vals = np.array([p[1] for p in paired], dtype=float)
                
                mae = np.mean(np.abs(a_vals - b_vals))
                rmse = np.sqrt(np.mean((a_vals - b_vals) ** 2))

                # Within-1 on raw mean scores (no rounding)
                within1_count = np.sum(np.abs(a_vals - b_vals) <= 1)
                within1 = (within1_count / len(paired)) * 100

                # Kappa still uses rounded Likert labels
                a_likert = np.array([to_likert(v, args.min_rating, args.max_rating) for v in a_vals])
                b_likert = np.array([to_likert(v, args.min_rating, args.max_rating) for v in b_vals])
                likert_filtered = [(a, b) for a, b in zip(a_likert, b_likert) if a is not None and b is not None]
                if likert_filtered:
                    a_likert_vals = np.array([p[0] for p in likert_filtered], dtype=int)
                    b_likert_vals = np.array([p[1] for p in likert_filtered], dtype=int)
                    kappa = weighted_cohen_kappa_quadratic(
                        a_likert_vals, b_likert_vals, K=args.max_rating - args.min_rating + 1
                    )
                else:
                    kappa = np.nan
                
                # Signed error
                signed_err = mean_signed_error(b_vals, a_vals)

            mae_matrix.loc[ra, rb] = mae
            rmse_matrix.loc[ra, rb] = rmse
            within1_matrix.loc[ra, rb] = within1
            kappa_matrix.loc[ra, rb] = kappa
            signed_error_matrix.loc[ra, rb] = signed_err

    # Report pairwise matrices
    report_lines.append("\n## Pairwise MAE (lower is better)")
    report_lines.append(mae_matrix.to_markdown())

    report_lines.append("\n## Pairwise RMSE (lower is better)")
    report_lines.append(rmse_matrix.to_markdown())

    report_lines.append("\n## Pairwise Within-1 Agreement (higher is better)")
    report_lines.append(within1_matrix.to_markdown())

    report_lines.append("\n## Pairwise Quadratic Weighted Kappa (higher is better)")
    report_lines.append(kappa_matrix.to_markdown())

    report_lines.append("\n## Pairwise Signed Error (closer to 0 is better; positive = over-rate)")
    report_lines.append(signed_error_matrix.to_markdown())

    # LLM Average Agreement with Humans (enhanced)
    report_lines.append("\n## LLM Average Agreement with Humans")
    report_lines.append("| LLM | Avg MAE | MAE Std | Avg RMSE | RMSE Std | Within-1 % | Avg κ_w | κ_w Std | Signed Err | Signed Err Std |")
    report_lines.append("|-----|---------|---------|----------|----------|------------|--------|--------|------------|----------------|")

    for llm in llm_raters + ["LLM-Jury"]:
        if llm in raters:
            human_maes = [mae_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_rmses = [rmse_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_within1s = [within1_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_kappas = [kappa_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_signed_errs = [signed_error_matrix.loc[llm, h] for h in human_raters if h in raters]

            if human_maes:
                avg_mae = np.nanmean(human_maes)
                std_mae = np.nanstd(human_maes)
                avg_rmse = np.nanmean(human_rmses)
                std_rmse = np.nanstd(human_rmses)
                avg_within1 = np.nanmean(human_within1s)
                avg_kappa = np.nanmean(human_kappas)
                std_kappa = np.nanstd(human_kappas)
                avg_signed_err = np.nanmean(human_signed_errs)
                std_signed_err = np.nanstd(human_signed_errs)

                report_lines.append(
                    f"| {llm} | {avg_mae:.4f} | {std_mae:.4f} | {avg_rmse:.4f} | {std_rmse:.4f} | "
                    f"{avg_within1:.2f} | {avg_kappa:.4f} | {std_kappa:.4f} | {avg_signed_err:.4f} | {std_signed_err:.4f} |"
                )

    # Human-Human Agreement (enhanced)
    report_lines.append("\n## Human-Human Agreement")
    report_lines.append("| Rater Pair | MAE | RMSE | Within-1 % | κ_w | Signed Err |")
    report_lines.append("|-----|-----|-----|------------|-----|------------|")

    human_maes_list = []
    human_rmses_list = []
    human_within1s_list = []
    human_kappas_list = []
    human_signed_errs_list = []

    for i, h1 in enumerate(human_raters):
        for h2 in human_raters[i + 1 :]:
            if h1 in raters and h2 in raters:
                mae_val = mae_matrix.loc[h1, h2]
                rmse_val = rmse_matrix.loc[h1, h2]
                within1_val = within1_matrix.loc[h1, h2]
                kappa_val = kappa_matrix.loc[h1, h2]
                signed_err_val = signed_error_matrix.loc[h1, h2]

                report_lines.append(
                    f"| {h1} vs {h2} | {mae_val:.4f} | {rmse_val:.4f} | {within1_val:.2f} | {kappa_val:.4f} | {signed_err_val:.4f} |"
                )
                human_maes_list.append(mae_val)
                human_rmses_list.append(rmse_val)
                human_within1s_list.append(within1_val)
                human_kappas_list.append(kappa_val)
                human_signed_errs_list.append(signed_err_val)

    if human_maes_list:
        avg_human_mae = np.nanmean(human_maes_list)
        std_human_mae = np.nanstd(human_maes_list)
        avg_human_rmse = np.nanmean(human_rmses_list)
        std_human_rmse = np.nanstd(human_rmses_list)
        avg_human_within1 = np.nanmean(human_within1s_list)
        avg_human_kappa = np.nanmean(human_kappas_list)
        std_human_kappa = np.nanstd(human_kappas_list)
        avg_human_signed_err = np.nanmean(human_signed_errs_list)
        std_human_signed_err = np.nanstd(human_signed_errs_list)

        report_lines.append(
            f"| **Avg** | **{avg_human_mae:.4f}** | **{avg_human_rmse:.4f}** | **{avg_human_within1:.2f}** | "
            f"**{avg_human_kappa:.4f}** | **{avg_human_signed_err:.4f}** |"
        )
        report_lines.append(
            f"| **Std Dev** | **{std_human_mae:.4f}** | **{std_human_rmse:.4f}** | -- | **{std_human_kappa:.4f}** | **{std_human_signed_err:.4f}** |"
        )

    # LLM Self-Consistency
    report_lines.append("\n## LLM Self-Consistency (3 stochastic runs)")
    report_lines.append("| LLM | Intra-LLM MAE ↓ | Intra-LLM κ_w ↑ | Range >= 2 % ↓ |")
    report_lines.append("|-----|-----------------|-----------------|----------------|")

    for llm in llm_raters:
        llm_dir = f"data/llm_evaluator/{llm}/n_200/merged"
        if os.path.exists(llm_dir):
            consistency = compute_intra_llm_consistency(sampled, llm_dir, args.min_rating, args.max_rating)
            mae_val = consistency.get("intra_llm_mae", np.nan)
            kappa_val = consistency.get("intra_llm_kappa_w", np.nan)
            range_val = consistency.get("range_ge_2_rate", np.nan)

            mae_str = f"{mae_val:.4f}" if not np.isnan(mae_val) else "N/A"
            kappa_str = f"{kappa_val:.4f}" if not np.isnan(kappa_val) else "N/A"
            range_str = f"{range_val:.2f}" if not np.isnan(range_val) else "N/A"

            report_lines.append(f"| {llm} | {mae_str} | {kappa_str} | {range_str} |")

    # Build raw (unrolled) LLM evaluations per item key
    raw_evals_by_key = {llm: {} for llm in llm_raters}
    sampled_keys = {make_key(item.get("inputs"), item.get("answer")) for item in sampled}

    for llm_name in llm_raters:
        merged_dir = os.path.join(f"data/llm_evaluator/{llm_name}/n_200/merged")
        merged_files = glob.glob(os.path.join(merged_dir, "*.json"))

        for merged_file in merged_files:
            try:
                with open(merged_file, "r", encoding="utf-8") as f:
                    merged_data = json.load(f)
                    if isinstance(merged_data, list):
                        for item in merged_data:
                            key = make_key(item.get("inputs"), item.get("answer"))
                            if key in sampled_keys and key not in raw_evals_by_key[llm_name]:
                                raw_evals_by_key[llm_name][key] = item.get("evals", [])
            except Exception:
                pass

    def build_unrolled_pairs(llm_name: str, human_rater: str) -> Tuple[List[int], List[int]]:
        llm_vals = []
        human_vals = []
        llm_map = raw_evals_by_key.get(llm_name, {})

        for idx, item in enumerate(sampled):
            human_score = rater_scores[human_rater][idx]
            if not is_valid_score(human_score):
                continue

            key = make_key(item.get("inputs"), item.get("answer"))
            evals = llm_map.get(key)
            if not evals:
                continue

            for e in evals[:3]:
                if not is_valid_score(e):
                    continue
                llm_vals.append(to_likert(e, args.min_rating, args.max_rating))
                human_vals.append(to_likert(human_score, args.min_rating, args.max_rating))

        filtered = [(l, h) for l, h in zip(llm_vals, human_vals) if l is not None and h is not None]
        if not filtered:
            return [], []

        llm_vals = [p[0] for p in filtered]
        human_vals = [p[1] for p in filtered]
        return llm_vals, human_vals

    # Confusion matrix summaries (unrolled LLM evaluations vs human)
    report_lines.append("\n## Confusion Matrix Summaries (Unrolled LLM Evaluations vs Human)")
    report_lines.append(
        "Note: Uses all 3 LLM evaluations per item (unrolled), compared against each human rater."
    )

    summary_data = []
    for llm_name in llm_raters:
        for h_rater in human_raters:
            if h_rater not in raters:
                continue

            llm_vals, human_vals = build_unrolled_pairs(llm_name, h_rater)
            if llm_vals and human_vals:
                summary = confusion_matrix_summary(human_vals, llm_vals)
                summary_data.append({
                    "Pair": f"{llm_name} vs {h_rater}",
                    "Exact %": summary.get("exact_agreement_pct", np.nan),
                    "Within-1 %": summary.get("within_1_pct", np.nan),
                    "Over %": summary.get("over_pct", np.nan),
                    "Under %": summary.get("under_pct", np.nan),
                    "Signed Err": summary.get("signed_error", np.nan),
                })

    # Human vs human summaries (no unrolling)
    for i, h1 in enumerate(human_raters):
        for h2 in human_raters[i + 1 :]:
            if h1 not in raters or h2 not in raters:
                continue

            paired = [
                (a, b)
                for a, b in zip(rater_scores[h1], rater_scores[h2])
                if is_valid_score(a) and is_valid_score(b)
            ]
            if not paired:
                continue

            a_vals = [to_likert(p[0], args.min_rating, args.max_rating) for p in paired]
            b_vals = [to_likert(p[1], args.min_rating, args.max_rating) for p in paired]
            filtered = [(a, b) for a, b in zip(a_vals, b_vals) if a is not None and b is not None]
            if not filtered:
                continue

            a_likert = [p[0] for p in filtered]
            b_likert = [p[1] for p in filtered]
            summary = confusion_matrix_summary(a_likert, b_likert)
            summary_data.append({
                "Pair": f"{h1} vs {h2}",
                "Exact %": summary.get("exact_agreement_pct", np.nan),
                "Within-1 %": summary.get("within_1_pct", np.nan),
                "Over %": summary.get("over_pct", np.nan),
                "Under %": summary.get("under_pct", np.nan),
                "Signed Err": summary.get("signed_error", np.nan),
            })

    # LLM-Jury summaries (per-item, not unrolled)
    if "LLM-Jury" in raters:
        for h_rater in human_raters:
            if h_rater not in raters:
                continue

            paired = [
                (a, b)
                for a, b in zip(rater_scores["LLM-Jury"], rater_scores[h_rater])
                if is_valid_score(a) and is_valid_score(b)
            ]
            if not paired:
                continue

            jury_vals = [to_likert(p[0], args.min_rating, args.max_rating) for p in paired]
            human_vals = [to_likert(p[1], args.min_rating, args.max_rating) for p in paired]
            filtered = [(j, h) for j, h in zip(jury_vals, human_vals) if j is not None and h is not None]
            if not filtered:
                continue

            jury_likert = [p[0] for p in filtered]
            human_likert = [p[1] for p in filtered]
            summary = confusion_matrix_summary(human_likert, jury_likert)
            summary_data.append({
                "Pair": f"LLM-Jury vs {h_rater}",
                "Exact %": summary.get("exact_agreement_pct", np.nan),
                "Within-1 %": summary.get("within_1_pct", np.nan),
                "Over %": summary.get("over_pct", np.nan),
                "Under %": summary.get("under_pct", np.nan),
                "Signed Err": summary.get("signed_error", np.nan),
            })

    if summary_data:
        df_summary = pd.DataFrame(summary_data)
        report_lines.append(df_summary.to_markdown(index=False))

        # LLM mean summary across humans
        df_summary["LLM"] = df_summary["Pair"].str.split(" vs ").str[0]
        summary_mean = (
            df_summary[df_summary["LLM"].isin(llm_raters + ["LLM-Jury"])]
            .groupby("LLM")[
                ["Exact %", "Within-1 %", "Over %", "Under %", "Signed Err"]
            ]
            .mean()
            .reset_index()
        )

        report_lines.append("\n### LLM Mean Summary (Unrolled vs Humans)")
        report_lines.append(
            "Note: Mean of each metric across all human raters for each LLM (LLM-Jury is per-item)."
        )
        report_lines.append(summary_mean.to_markdown(index=False))

    # Confusion matrices (unrolled LLM evaluations vs human)
    report_lines.append("\n## Confusion Matrices (Unrolled LLM Evaluations vs Human)")
    report_lines.append(
        "Note: Uses all 3 LLM evaluations per item (unrolled) and rounded to 1–5 Likert."
    )
    labels = list(range(args.min_rating, args.max_rating + 1))

    for llm_name in llm_raters:
        for h_rater in human_raters:
            if h_rater not in raters:
                continue

            llm_vals, human_vals = build_unrolled_pairs(llm_name, h_rater)
            if llm_vals and human_vals:
                cm = confusion_matrix(llm_vals, human_vals, labels=labels)
                df_cm = pd.DataFrame(cm, index=labels, columns=labels)
                report_lines.append(
                    f"\n### {llm_name} evals (rows) vs {h_rater} (cols) — {len(llm_vals)} evals"
                )
                report_lines.append(df_cm.to_markdown())

    # LLM-Jury confusion matrices (per-item, not unrolled)
    if "LLM-Jury" in raters:
        report_lines.append("\n## Confusion Matrices (LLM-Jury vs Human)")
        report_lines.append(
            "Note: Uses per-item LLM-Jury scores (mean across LLMs), rounded to 1–5 Likert."
        )

        for h_rater in human_raters:
            if h_rater not in raters:
                continue

            paired = [
                (a, b)
                for a, b in zip(rater_scores["LLM-Jury"], rater_scores[h_rater])
                if is_valid_score(a) and is_valid_score(b)
            ]
            if not paired:
                continue

            jury_vals = [to_likert(p[0], args.min_rating, args.max_rating) for p in paired]
            human_vals = [to_likert(p[1], args.min_rating, args.max_rating) for p in paired]
            filtered = [(j, h) for j, h in zip(jury_vals, human_vals) if j is not None and h is not None]
            if not filtered:
                continue

            jury_likert = [p[0] for p in filtered]
            human_likert = [p[1] for p in filtered]
            cm = confusion_matrix(jury_likert, human_likert, labels=labels)
            df_cm = pd.DataFrame(cm, index=labels, columns=labels)
            report_lines.append(
                f"\n### LLM-Jury evals (rows) vs {h_rater} (cols) — {len(jury_likert)} evals"
            )
            report_lines.append(df_cm.to_markdown())

    # Save outputs
    ensure_dir(args.output_dir)
    report_path = os.path.join(args.output_dir, "appropriateness_agreement_enhanced_report.md")
    mae_path = os.path.join(args.output_dir, "pairwise_mae.csv")
    rmse_path = os.path.join(args.output_dir, "pairwise_rmse.csv")
    within1_path = os.path.join(args.output_dir, "pairwise_within1.csv")
    kappa_path = os.path.join(args.output_dir, "pairwise_kappa.csv")
    signed_error_path = os.path.join(args.output_dir, "pairwise_signed_error.csv")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    mae_matrix.to_csv(mae_path)
    rmse_matrix.to_csv(rmse_path)
    within1_matrix.to_csv(within1_path)
    kappa_matrix.to_csv(kappa_path)
    signed_error_matrix.to_csv(signed_error_path)

    print(f"Report saved to: {report_path}")
    print(f"Pairwise MAE saved to: {mae_path}")
    print(f"Pairwise RMSE saved to: {rmse_path}")
    print(f"Pairwise Within-1 saved to: {within1_path}")
    print(f"Pairwise Kappa saved to: {kappa_path}")
    print(f"Pairwise Signed Error saved to: {signed_error_path}")


if __name__ == "__main__":
    main()
