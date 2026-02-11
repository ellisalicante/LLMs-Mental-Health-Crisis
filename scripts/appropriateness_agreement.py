"""
Appropriateness Agreement Analysis Script

Computes inter-rater agreement statistics for crisis appropriateness scores (1-5 Likert scale)
across human raters and LLM evaluators.

USAGE:
    python scripts/appropriateness_agreement.py

OPTIONS:
    --sampled-path PATH             Path to sampled dataset JSON (default: data/llm_evaluator/sampled/sampled_lowest_scores_n200.json)
    --evaluator-paths NAME=PATH ... LLM evaluator paths as 'name=path' pairs (auto-detected from data/llm_evaluator/*/n_200/merged if not provided)
    --human-score-paths PATH ...    Human score XLSX files (auto-detected from data/human_label/*_scores_n206_s42.xlsx if not provided)
    --output-dir DIR                Output directory (default: outputs/appropriateness_agreement)
    --min-rating INT                Minimum rating value (default: 1)
    --max-rating INT                Maximum rating value (default: 5)

OUTPUTS:
    outputs/appropriateness_agreement/appropriateness_agreement_report.md
        - Rater coverage and score counts
        - Pairwise MAE matrix (all rater pairs)
        - LLM Average Agreement with Humans
        - Human-Human Agreement
        - 10 confusion matrices (mean scores for all pairwise combinations)
        - 3 confusion matrices (LLM raw evals vs all humans combined)
        - 6 confusion matrices (LLM raw evals vs each human rater individually)
    
    outputs/appropriateness_agreement/pairwise_mae.csv
        - Pairwise MAE matrix in CSV format

METRICS:
    - MAE: Mean Absolute Error on 1-5 scale (lower is better)
    - Confusion Matrices: Rounded to nearest integer using half-up rounding (e.g., 3.5 -> 4)
    - Raw Evaluations: LLMs generate 3 evaluations per response; this includes all 3 (570 total per LLM)
"""

import argparse
import ast
import glob
import json
import math
import os
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


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

    # Return scores in order (NaN for missing)
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
                    print(
                        f"WARNING: Conflicting scores for key in {file_path} vs {prev_file}. "
                        f"Keeping first: {prev_score}"
                    )
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


def main():
    parser = argparse.ArgumentParser(description="Compute Human/LLM agreement on appropriateness scores.")
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
        default="outputs/appropriateness_agreement",
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
    args = parser.parse_args()

    sampled = load_json(args.sampled_path)
    print(f"Loaded sampled set: {len(sampled)} items")

    rater_scores: Dict[str, List[float]] = {}
    rater_sources: Dict[str, Dict[str, str]] = {}

    # gpt-4o-mini scores from sampled file
    gpt4o_scores = [item.get("evaluation", None) for item in sampled]
    rater_scores["gpt-4o-mini"] = gpt4o_scores

    # LLM evaluator scores
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
        sources = {}
        for item in sampled:
            key = make_key(item.get("inputs"), item.get("answer"))
            if key in score_map:
                score, src = score_map[key]
                aligned.append(score)
                sources[key] = src
            else:
                aligned.append(None)
        rater_scores[name] = aligned
        rater_sources[name] = sources

        # Write extracted file
        extracted_path = os.path.join(
            "data/llm_evaluator/sampled",
            f"sampled_lowest_scores_n200__{name}.json",
        )
        ensure_dir(os.path.dirname(extracted_path))
        extracted = []
        for item in sampled:
            key = make_key(item.get("inputs"), item.get("answer"))
            extracted.append(
                {
                    "inputs": item.get("inputs"),
                    "answer": item.get("answer"),
                    "label": item.get("label"),
                    "dataset_id": item.get("dataset_id"),
                    "evaluation": score_map.get(key, (None, None))[0],
                    "source_file": score_map.get(key, (None, None))[1],
                }
            )
        with open(extracted_path, "w", encoding="utf-8") as f:
            json.dump(extracted, f, ensure_ascii=False, indent=2)
        print(f"Saved extracted scores: {extracted_path}")

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

    # Pairwise MAE matrix
    raters = list(rater_scores.keys())
    
    # Create LLM Jury (mean of 3 LLMs)
    llm_raters = ["gpt-4o-mini", "gpt-5-nano", "meta-llama"]
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
    
    raters = list(rater_scores.keys())
    mae_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    rmse_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    within1_matrix = pd.DataFrame(index=raters, columns=raters, dtype=float)
    report_lines = []
    report_lines.append("# Appropriateness Agreement Report")
    report_lines.append("\n## Rater coverage")
    for r in raters:
        non_null = sum(1 for x in rater_scores[r] if is_valid_score(x))
        report_lines.append(f"- {r}: {non_null} scored / {len(sampled)}")

    report_lines.append("\n## Pairwise MAE (lower is better)")
    llm_raters = ["gpt-4o-mini", "gpt-5-nano", "meta-llama"]
    human_raters = [r for r in raters if r not in llm_raters and r != "LLM-Jury"]
    
    for i, ra in enumerate(raters):
        for j, rb in enumerate(raters):
            if i == j:
                mae_matrix.loc[ra, rb] = 0.0
                rmse_matrix.loc[ra, rb] = 0.0
                within1_matrix.loc[ra, rb] = 100.0
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
            else:
                a_vals = np.array([p[0] for p in paired], dtype=float)
                b_vals = np.array([p[1] for p in paired], dtype=float)
                mae = np.mean(np.abs(a_vals - b_vals))
                rmse = np.sqrt(np.mean((a_vals - b_vals) ** 2))
                within1_count = np.sum(np.abs(a_vals - b_vals) <= 1)
                within1 = (within1_count / len(paired)) * 100
            mae_matrix.loc[ra, rb] = mae
            rmse_matrix.loc[ra, rb] = rmse
            within1_matrix.loc[ra, rb] = within1

    report_lines.append(mae_matrix.to_markdown())
    
    report_lines.append("\n## Pairwise RMSE (lower is better)")
    report_lines.append(rmse_matrix.to_markdown())
    
    report_lines.append("\n## Pairwise Within-1 Agreement (higher is better)")
    report_lines.append(within1_matrix.to_markdown())
    
    # Add LLM-average-human MAE and RMSE with std
    report_lines.append("\n## LLM Average Agreement with Humans")
    report_lines.append("| LLM | Avg MAE | MAE Std | Avg RMSE | RMSE Std | Within-1 % |")
    report_lines.append("|-----|---------|---------|----------|----------|------------|")
    for llm in llm_raters + ["LLM-Jury"]:
        if llm in raters:
            human_maes = [mae_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_rmses = [rmse_matrix.loc[llm, h] for h in human_raters if h in raters]
            human_within1s = [within1_matrix.loc[llm, h] for h in human_raters if h in raters]
            if human_maes and human_rmses:
                avg_mae = np.nanmean(human_maes)
                std_mae = np.nanstd(human_maes)
                avg_rmse = np.nanmean(human_rmses)
                std_rmse = np.nanstd(human_rmses)
                avg_within1 = np.nanmean(human_within1s)
                report_lines.append(f"| {llm} | {avg_mae:.6f} | {std_mae:.6f} | {avg_rmse:.6f} | {std_rmse:.6f} | {avg_within1:.2f} |")
    
    # Add human-human agreement with std
    report_lines.append("\n## Human-Human Agreement")
    report_lines.append("| Rater Pair | MAE | RMSE | Within-1 % |")
    report_lines.append("|-----|-----|-----|------------|")
    human_maes_list = []
    human_rmses_list = []
    human_within1s_list = []
    for i, h1 in enumerate(human_raters):
        for h2 in human_raters[i+1:]:
            if h1 in raters and h2 in raters:
                mae_val = mae_matrix.loc[h1, h2]
                rmse_val = rmse_matrix.loc[h1, h2]
                within1_val = within1_matrix.loc[h1, h2]
                report_lines.append(f"| {h1} vs {h2} | {mae_val:.6f} | {rmse_val:.6f} | {within1_val:.2f} |")
                human_maes_list.append(mae_val)
                human_rmses_list.append(rmse_val)
                human_within1s_list.append(within1_val)
    if human_maes_list:
        avg_human_mae = np.nanmean(human_maes_list)
        std_human_mae = np.nanstd(human_maes_list)
        avg_human_rmse = np.nanmean(human_rmses_list)
        std_human_rmse = np.nanstd(human_rmses_list)
        avg_human_within1 = np.nanmean(human_within1s_list)
        report_lines.append(f"| **Avg** | **{avg_human_mae:.6f}** | **{avg_human_rmse:.6f}** | **{avg_human_within1:.2f}** |")
        report_lines.append(f"| **Std Dev** | **{std_human_mae:.6f}** | **{std_human_rmse:.6f}** | -- |")

    # Confusion matrices
    report_lines.append("\n## Confusion Matrices (rounded to nearest integer, 1-5)")
    report_lines.append(
        "Note: scores are rounded using half-up (e.g., 3.5 → 4) and clipped to the [1, 5] range."
    )
    labels = list(range(args.min_rating, args.max_rating + 1))
    for i in range(len(raters)):
        for j in range(i + 1, len(raters)):
            ra = raters[i]
            rb = raters[j]
            paired = [
                (a, b)
                for a, b in zip(rater_scores[ra], rater_scores[rb])
                if is_valid_score(a) and is_valid_score(b)
            ]
            if not paired:
                continue
            a_vals = [to_likert(p[0], args.min_rating, args.max_rating) for p in paired]
            b_vals = [to_likert(p[1], args.min_rating, args.max_rating) for p in paired]
            filtered = [(a, b) for a, b in zip(a_vals, b_vals) if a is not None and b is not None]
            if not filtered:
                continue
            a_vals = [p[0] for p in filtered]
            b_vals = [p[1] for p in filtered]
            cm = confusion_matrix(a_vals, b_vals, labels=labels)
            df_cm = pd.DataFrame(cm, index=labels, columns=labels)
            report_lines.append(f"\n### {ra} (rows) vs {rb} (cols)")
            report_lines.append(df_cm.to_markdown())

    # Confusion matrices with raw LLM evaluations (all 3 evals per response)
    report_lines.append("\n## Confusion Matrices: LLM Raw Evaluations vs Human (190 × 3 evals)")
    report_lines.append(
        "Note: LLMs evaluate each response 3 times. This CM includes all raw evaluations (190 responses × 3 = 570 evals)."
    )
    
    # Extract raw evaluations from merged directories for all LLMs
    raw_evals = {
        "gpt-4o-mini": [],
        "gpt-5-nano": [],
        "meta-llama": []
    }
    
    # Build key maps for matching items
    sampled_keys = {make_key(item.get("inputs"), item.get("answer")): item for item in sampled}
    
    # For each LLM, extract raw evals from merged directories
    for llm_name in llm_raters:
        merged_dir = os.path.join(f"data/llm_evaluator/{llm_name}/n_200/merged")
        merged_files = glob.glob(os.path.join(merged_dir, "*.json"))
        
        seen_keys = set()
        for merged_file in merged_files:
            try:
                with open(merged_file, "r", encoding="utf-8") as f:
                    merged_data = json.load(f)
                    if isinstance(merged_data, list):
                        for item in merged_data:
                            key = make_key(item.get("inputs"), item.get("answer"))
                            if key in sampled_keys and key not in seen_keys:
                                raw_evals[llm_name].extend(item.get("evals", []))
                                seen_keys.add(key)
            except Exception as e:
                pass
    
    # Create confusion matrices for each LLM with humans (using raw evals)
    for llm_name in llm_raters:
        if not raw_evals[llm_name]:
            continue
        
        # Repeat human scores 3 times to match raw evals
        human_repeated = []
        for h_rater in human_raters:
            if h_rater in raters:
                for score in rater_scores[h_rater]:
                    if is_valid_score(score):
                        human_repeated.extend([score] * 3)
        
        # Take only as many human scores as we have raw evals
        num_evals = min(len(raw_evals[llm_name]), len(human_repeated))
        llm_evals_vals = raw_evals[llm_name][:num_evals]
        human_evals_vals = human_repeated[:num_evals]
        
        if llm_evals_vals and human_evals_vals:
            llm_rounded = [to_likert(v, args.min_rating, args.max_rating) for v in llm_evals_vals]
            human_rounded = [to_likert(v, args.min_rating, args.max_rating) for v in human_evals_vals]
            filtered = [(l, h) for l, h in zip(llm_rounded, human_rounded) if l is not None and h is not None]
            
            if filtered:
                llm_vals = [p[0] for p in filtered]
                human_vals = [p[1] for p in filtered]
                cm = confusion_matrix(llm_vals, human_vals, labels=labels)
                df_cm = pd.DataFrame(cm, index=labels, columns=labels)
                report_lines.append(f"\n### {llm_name} raw evals (rows) vs Humans (cols) — {len(llm_vals)} evaluations")
                report_lines.append(df_cm.to_markdown())
    
    # Create confusion matrices for each LLM raw evals with each human rater separately
    report_lines.append("\n## Confusion Matrices: LLM Raw Evaluations vs Individual Human Raters")
    report_lines.append("Note: Raw evaluations (all 3 per response) compared against each human rater separately.")
    
    for llm_name in llm_raters:
        if not raw_evals[llm_name]:
            continue
        
        for h_rater in human_raters:
            if h_rater not in raters:
                continue
            
            # Repeat this human's scores 3 times to match raw evals
            human_scores = rater_scores[h_rater]
            human_repeated = []
            for score in human_scores:
                if is_valid_score(score):
                    human_repeated.extend([score] * 3)
            
            # Take only as many as we have raw evals
            num_evals = min(len(raw_evals[llm_name]), len(human_repeated))
            llm_evals_vals = raw_evals[llm_name][:num_evals]
            human_evals_vals = human_repeated[:num_evals]
            
            if llm_evals_vals and human_evals_vals:
                llm_rounded = [to_likert(v, args.min_rating, args.max_rating) for v in llm_evals_vals]
                human_rounded = [to_likert(v, args.min_rating, args.max_rating) for v in human_evals_vals]
                filtered = [(l, h) for l, h in zip(llm_rounded, human_rounded) if l is not None and h is not None]
                
                if filtered:
                    llm_vals = [p[0] for p in filtered]
                    human_vals = [p[1] for p in filtered]
                    cm = confusion_matrix(llm_vals, human_vals, labels=labels)
                    df_cm = pd.DataFrame(cm, index=labels, columns=labels)
                    report_lines.append(f"\n### {llm_name} raw evals (rows) vs {h_rater} (cols) — {len(llm_vals)} evaluations")
                    report_lines.append(df_cm.to_markdown())

    ensure_dir(args.output_dir)
    report_path = os.path.join(args.output_dir, "appropriateness_agreement_report.md")
    mae_path = os.path.join(args.output_dir, "pairwise_mae.csv")
    rmse_path = os.path.join(args.output_dir, "pairwise_rmse.csv")
    within1_path = os.path.join(args.output_dir, "pairwise_within1.csv")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    mae_matrix.to_csv(mae_path)
    rmse_matrix.to_csv(rmse_path)
    within1_matrix.to_csv(within1_path)

    print(f"Report saved to: {report_path}")
    print(f"Pairwise MAE saved to: {mae_path}")
    print(f"Pairwise RMSE saved to: {rmse_path}")
    print(f"Pairwise Within-1 Agreement saved to: {within1_path}")


if __name__ == "__main__":
    main()
