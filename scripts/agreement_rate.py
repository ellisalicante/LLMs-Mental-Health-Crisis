import json
import os
import argparse
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from statsmodels.stats.inter_rater import fleiss_kappa
import numpy as np
import sys
import pandas as pd
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.config import LABELS, LLM_LABEL_DIR, HUMAN_LABEL_DIR


LABELS_ORDERED = sorted(LABELS)


def build_label_list(base_labels, include_empty=True):
    """Return a stable label order for confusion matrices."""
    labels = list(base_labels)
    if include_empty:
        labels.append("")
    return labels


def compute_row_normalized_confusion(cm, labels):
    """Compute row-normalized confusion P(B|A) with safe zero-row handling."""
    cm = np.asarray(cm, dtype=float)
    row_sums = cm.sum(axis=1)
    row_norm = np.zeros_like(cm, dtype=float)
    for idx, row_sum in enumerate(row_sums):
        if row_sum > 0:
            row_norm[idx] = cm[idx] / row_sum
    return row_norm, row_sums


def summarize_most_confused_per_label(cm, labels, exclude_labels=None):
    """Return per-label most confused target based on row-normalized P(B|A)."""
    exclude_labels = set(exclude_labels or [])
    row_norm, row_sums = compute_row_normalized_confusion(cm, labels)
    results = []
    for idx, label in enumerate(labels):
        if label in exclude_labels:
            continue
        if row_sums[idx] <= 0:
            results.append({
                "label": label,
                "confused_with": None,
                "probability": None,
                "support": int(row_sums[idx])
            })
            continue

        row = row_norm[idx].copy()
        row[idx] = -1.0
        top_j = int(np.argmax(row))
        top_p = float(row_norm[idx, top_j])
        if top_p <= 0.0:
            results.append({
                "label": label,
                "confused_with": None,
                "probability": None,
                "support": int(row_sums[idx])
            })
        else:
            results.append({
                "label": label,
                "confused_with": labels[top_j],
                "probability": top_p,
                "support": int(row_sums[idx])
            })
    return results, row_norm


def compute_s_balanced(row_norm, labels, exclude_labels=None):
    """Compute symmetric confusion scores s_balanced for label pairs."""
    exclude_labels = set(exclude_labels or [])
    pairs = []
    for i, label_i in enumerate(labels):
        if label_i in exclude_labels:
            continue
        for j in range(i + 1, len(labels)):
            label_j = labels[j]
            if label_j in exclude_labels:
                continue
            score = float(row_norm[i, j] + row_norm[j, i])
            pairs.append({
                "label_i": label_i,
                "label_j": label_j,
                "score": score,
                "p_i_to_j": float(row_norm[i, j]),
                "p_j_to_i": float(row_norm[j, i])
            })
    pairs.sort(key=lambda item: item["score"], reverse=True)
    return pairs


def build_s_balanced_matrix(row_norm, labels, exclude_labels=None):
    """Build a symmetric s_balanced matrix aligned to labels."""
    exclude_labels = set(exclude_labels or [])
    size = len(labels)
    matrix = np.zeros((size, size), dtype=float)
    for i, label_i in enumerate(labels):
        for j, label_j in enumerate(labels):
            if i == j:
                continue
            if label_i in exclude_labels or label_j in exclude_labels:
                continue
            matrix[i, j] = float(row_norm[i, j] + row_norm[j, i])
    return matrix


def format_most_confused_table(results):
    """Format per-label confusion summary into markdown table rows."""
    lines = []
    lines.append("| Label A | Most Confused As B | P(B\\|A) | Support |")
    lines.append("|---------|---------------------|--------|---------|")
    for row in results:
        if row["confused_with"] is None:
            lines.append(f"| {row['label']} | n/a | n/a | {row['support']} |")
        else:
            lines.append(
                f"| {row['label']} | {row['confused_with']} | {row['probability']:.3f} | {row['support']} |"
            )
    return lines


def format_top_pairs_table(pairs, top_k=5):
    """Format top symmetric confusion pairs into markdown table rows."""
    lines = []
    lines.append("| Label i | Label j | s_balanced | P(j\\|i) | P(i\\|j) |")
    lines.append("|---------|---------|-----------:|-------:|-------:|")
    for row in pairs[:top_k]:
        lines.append(
            f"| {row['label_i']} | {row['label_j']} | {row['score']:.3f} | {row['p_i_to_j']:.3f} | {row['p_j_to_i']:.3f} |"
        )
    return lines


def sanitize_filename(name, max_length=120):
    """Make a string safe for filenames, with length guard."""
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_") or "unnamed"
    if len(safe) <= max_length:
        return safe
    digest = str(abs(hash(safe)))
    keep = max_length - len(digest) - 1
    return f"{safe[:keep]}_{digest}"


def pairs_to_dataframe(pairs):
    """Convert s_balanced pair list into a dataframe."""
    return pd.DataFrame(
        [
            {
                "label_i": row["label_i"],
                "label_j": row["label_j"],
                "s_balanced": row["score"],
                "p_j_given_i": row["p_i_to_j"],
                "p_i_given_j": row["p_j_to_i"],
            }
            for row in pairs
        ]
    )


def per_label_summary_to_dataframe(summary_rows):
    """Convert per-label confusion summary into a dataframe."""
    return pd.DataFrame(summary_rows)


def write_pair_csvs(output_dir, pair_label, labels, cm, row_norm, s_balanced_matrix, per_label_summary, pair_scores):
    """Write per-pair CSV tables for confusion and summaries."""
    pair_dir = os.path.join(output_dir, "pairs")
    os.makedirs(pair_dir, exist_ok=True)
    base = sanitize_filename(pair_label)

    pd.DataFrame(cm, index=labels, columns=labels).to_csv(
        os.path.join(pair_dir, f"{base}__confusion_counts.csv")
    )
    pd.DataFrame(row_norm, index=labels, columns=labels).to_csv(
        os.path.join(pair_dir, f"{base}__confusion_row_norm.csv")
    )
    pd.DataFrame(s_balanced_matrix, index=labels, columns=labels).to_csv(
        os.path.join(pair_dir, f"{base}__s_balanced_matrix.csv")
    )
    per_label_summary_to_dataframe(per_label_summary).to_csv(
        os.path.join(pair_dir, f"{base}__most_confused_labels.csv"),
        index=False
    )
    pairs_to_dataframe(pair_scores).to_csv(
        os.path.join(pair_dir, f"{base}__most_confused_pairs.csv"),
        index=False
    )


def compute_confusion_summary_for_pairs(annotations, pair_keys, labels, exclude_labels=None):
    """Aggregate confusion across rater pairs and compute summary tables."""
    if not pair_keys:
        return None

    total_cm = np.zeros((len(labels), len(labels)), dtype=int)
    for name_A, name_B in pair_keys:
        labels_A = [item["label"] for item in annotations[name_A]]
        labels_B = [item["label"] for item in annotations[name_B]]
        cm = confusion_matrix(labels_A, labels_B, labels=labels)
        total_cm += cm

    per_label, row_norm = summarize_most_confused_per_label(
        total_cm,
        labels,
        exclude_labels=exclude_labels
    )
    pair_scores = compute_s_balanced(row_norm, labels, exclude_labels=exclude_labels)
    return {
        "per_label": per_label,
        "pair_scores": pair_scores,
        "pair_count": len(pair_keys),
        "row_norm": row_norm
    }


def append_confusion_summary(report_lines, title, annotations, pair_keys, labels, exclude_labels=None, top_k=5, output_dir=None, csv_prefix=None):
    """Append a summary block for most confused labels and label pairs."""
    summary = compute_confusion_summary_for_pairs(
        annotations,
        pair_keys,
        labels,
        exclude_labels=exclude_labels
    )
    report_lines.append(title)
    if summary is None:
        report_lines.append("No rater pairs available for this summary.")
        report_lines.append('---')
        return

    report_lines.append(f"- Rater pairs: {summary['pair_count']}")
    report_lines.append("")
    s_balanced_matrix = build_s_balanced_matrix(
        summary["row_norm"],
        labels,
        exclude_labels=exclude_labels
    )
    report_lines.append("s_balanced matrix (s(i,j) = P(j\\|i) + P(i\\|j)):")
    s_balanced_df = pd.DataFrame(
        s_balanced_matrix,
        index=labels,
        columns=labels
    )
    report_lines.append(s_balanced_df.to_markdown())
    report_lines.append('')
    report_lines.append('')
    report_lines.append("Most confused labels (row-normalized P(B\\|A)):")
    report_lines.extend(format_most_confused_table(summary["per_label"]))
    report_lines.append('')

    report_lines.append("Most confused label pairs (s_balanced):")
    if summary["pair_scores"]:
        report_lines.extend(format_top_pairs_table(summary["pair_scores"], top_k=top_k))
    else:
        report_lines.append("No label pairs available for s_balanced.")
    report_lines.append('---')

    if output_dir and csv_prefix:
        summary_dir = os.path.join(output_dir, "summaries")
        os.makedirs(summary_dir, exist_ok=True)
        pd.DataFrame(s_balanced_matrix, index=labels, columns=labels).to_csv(
            os.path.join(summary_dir, f"{csv_prefix}__s_balanced_matrix.csv")
        )
        per_label_summary_to_dataframe(summary["per_label"]).to_csv(
            os.path.join(summary_dir, f"{csv_prefix}__most_confused_labels.csv"),
            index=False
        )
        pairs_to_dataframe(summary["pair_scores"]).to_csv(
            os.path.join(summary_dir, f"{csv_prefix}__most_confused_pairs.csv"),
            index=False
        )


def compute_fleiss_kappa(annotation_dict, labels_to_use):
    label_to_idx = {label: i for i, label in enumerate(labels_to_use)}
    num_categories = len(labels_to_use)
    num_items = len(original_data)
    #num_annotators = len(annotation_dict)

    # Matrix of shape (n_items, n_categories)
    # Each row contains counts of how many annotators assigned each label to that item
    fleiss_matrix = np.zeros((num_items, num_categories), dtype=int)

    for item_idx in range(num_items):
        label_counts = [0] * num_categories
        for annotator in annotation_dict.values():
            label = annotator[item_idx]["label"]
            if label not in label_to_idx:
                raise ValueError(f"Label '{label}' not in LABELS.")
            label_idx = label_to_idx[label]
            label_counts[label_idx] += 1
        fleiss_matrix[item_idx] = label_counts

    # Compute Fleiss' Kappa
    return fleiss_kappa(fleiss_matrix)


def calculate_agreement_rate(labels_A, labels_B):    
    agreement_count = sum(1 for a, b in zip(labels_A, labels_B) if a == b)
    return agreement_count / len(labels_A) * 100

argparser = argparse.ArgumentParser(description="Calculate agreement rate between two or more labeled datasets.")
argparser.add_argument("--human_paths", nargs="+", required=False, help="Paths to the human-labeled JSON files to compare.")
argparser.add_argument("--llm_paths", nargs="+", required=False, help="Paths to the llm-labeled JSON files to compare.")
argparser.add_argument("--original_path", type=str, required=True, help="Path to the original unlabeled json.")
argparser.add_argument("--output_dir", type=str, default=os.path.join("outputs", "appropriateness_agreement"), help="Directory to save the report.")
argparser.add_argument("--write_csv", action="store_true", help="Write CSV tables alongside the markdown report.")

args = argparser.parse_args()
human_paths = args.human_paths
human_paths = [human_paths] if isinstance(human_paths, str) else human_paths
llm_paths = args.llm_paths
llm_paths = [llm_paths] if isinstance(llm_paths, str) else llm_paths
original_path = args.original_path
report_lines = []
labels_all = build_label_list(LABELS_ORDERED, include_empty=True)
exclude_analysis_labels = {""}

#* Read files
with open(os.path.join(original_path), "r", encoding="utf-8") as f:
    original_data = json.load(f)

if human_paths:
    human_annotations_dict = {}
    for path in human_paths:
        with open(os.path.join(HUMAN_LABEL_DIR, path), "r", encoding="utf-8") as f:
            name_annotation = os.path.basename(path)
            human_annotations_dict[name_annotation] = json.load(f)

if llm_paths:
    llm_annotations_dict= {}
    llm_families = {}
    for path in llm_paths:
        with open(os.path.join(LLM_LABEL_DIR, path), "r", encoding="utf-8") as f:
            name_annotation = os.path.basename(path)
            llm_annotations_dict[name_annotation] = json.load(f)
        llm_name = name_annotation.split('-labeled')[0]
        llm_families.setdefault(llm_name, []).append(name_annotation)


#* check that all inputs are the same as the original data - same number and same order.
if human_paths:
    for human_key in human_annotations_dict:
        for idx_sample, item in enumerate(original_data):
            if human_annotations_dict[human_key][idx_sample]["inputs"] != item["inputs"]:
                raise ValueError(f"Mismatch in inputs at index {idx_sample}. Human annotation {human_key} does not match original data.")

if llm_paths:
    for llm_key in llm_annotations_dict:
        for idx_sample, item in enumerate(original_data):
            if llm_annotations_dict[llm_key][idx_sample]["inputs"] != item["inputs"]:
                raise ValueError(f"Mismatch in inputs at index {idx_sample}. LLM annotation {llm_key} does not match original data.")


#* Prepare report header
report_lines.append("# Agreement Rate Report")
report_lines.append('## Dataset Summary')
report_lines.append(f"- Total number of conversations: {len(original_data)}")
if human_paths:
    report_lines.append(f"- Human annotators: {len(human_annotations_dict)}")
    for human_key in human_annotations_dict:
        report_lines.append(f"    * {human_key}: {len(human_annotations_dict[human_key])} annotations")
if llm_paths:
    report_lines.append(f"- LLM annotators: {len(llm_annotations_dict)}")
    for llm_key in llm_annotations_dict:
        report_lines.append(f"    * {llm_key}: {len(llm_annotations_dict[llm_key])} annotations")


if llm_paths and human_paths:
    all_annotations = {**human_annotations_dict, **llm_annotations_dict}
elif llm_paths:
    all_annotations = llm_annotations_dict
elif human_paths:
    all_annotations = human_annotations_dict
else:
    raise ValueError("At least one of --human_paths or --llm_paths must be provided.")

all_annotations_keys = list(all_annotations.keys())
human_keys = list(human_annotations_dict.keys()) if human_paths else []
llm_keys = list(llm_annotations_dict.keys()) if llm_paths else []


#* Calculate pairwise agreement rates
report_lines.append('## Pairwise Agreement Rates')
agreement_rates = []
for i in range(len(all_annotations_keys)):
    for j in range(i + 1, len(all_annotations_keys)):
        name_A = all_annotations_keys[i]
        name_B = all_annotations_keys[j]

        labels_A = [item["label"] for item in all_annotations[name_A]]
        labels_B = [item["label"] for item in all_annotations[name_B]]

        #assert all labels are in LABELS
        if not set(labels_A).issubset(labels_all):
            print(f"\nLabelsA: {set(labels_A)} -- LABELS: {LABELS}")
            raise ValueError(f"LabelsA in {name_A} are not a subset of defined LABELS.")
        if not set(labels_B).issubset(labels_all):
            print(f"LabelsB: {set(labels_B)} in {name_B} are not a subset of defined LABELS.")
            raise ValueError(f"LabelsB in {name_B} are not a subset of defined LABELS.")
        
        agreement_rate = calculate_agreement_rate(labels_A, labels_B)
        kappa_score = cohen_kappa_score(labels_A, labels_B, labels=labels_all)
        
        agreement_rates.append({"file_A": name_A, "file_B": name_B,
            "agreement_rate": agreement_rate,
            "cohen_kappa": kappa_score
        })
        
        #* Print results
        report_lines.append(f"### `{name_A}` and `{name_B}`:")
        report_lines.append(f"\t* 🟩 Agreement Rate: {agreement_rate:.2f}%")
        report_lines.append(f"\t* 🧠 Cohen's Kappa: {kappa_score:.2f}") 
        

        #Calculate confusion matrix
        cm = confusion_matrix(labels_A, labels_B, labels=labels_all)
        report_lines.append(f"Confusion Matrix between `{name_A}` (ROWS) and `{name_B}` (COLS):")
        df = pd.DataFrame(cm,
                          index=labels_all, # f"{name_A}: {l}" for l in labels_all]
                          columns=labels_all) # [f"{name_B}: {l}" for l in labels_all]
        report_lines.append(df.to_markdown())
        report_lines.append('')

        per_label_summary, row_norm = summarize_most_confused_per_label(
            cm,
            labels_all,
            exclude_labels=exclude_analysis_labels
        )
        s_balanced_matrix = build_s_balanced_matrix(
            row_norm,
            labels_all,
            exclude_labels=exclude_analysis_labels
        )
        report_lines.append("s_balanced matrix (s(i,j) = P(j\\|i) + P(i\\|j)):")
        s_balanced_df = pd.DataFrame(
            s_balanced_matrix,
            index=labels_all,
            columns=labels_all
        )
        report_lines.append(s_balanced_df.to_markdown())
        report_lines.append('')

        report_lines.append("Most confused labels (row-normalized P(B\\|A)):")
        report_lines.extend(format_most_confused_table(per_label_summary))
        report_lines.append('')

        pair_scores = compute_s_balanced(row_norm, labels_all, exclude_labels=exclude_analysis_labels)
        report_lines.append("Most confused label pairs (s_balanced):")
        if pair_scores:
            report_lines.extend(format_top_pairs_table(pair_scores, top_k=5))
        else:
            report_lines.append("No label pairs available for s_balanced.")
        report_lines.append('')

        if args.write_csv:
            pair_label = f"{name_A}__vs__{name_B}"
            write_pair_csvs(
                args.output_dir,
                pair_label,
                labels_all,
                cm,
                row_norm,
                s_balanced_matrix,
                per_label_summary,
                pair_scores
            )
        #report_lines.append(cm)
        #report_lines.append("-" * 40)


#*Fleiss kappa between humans
if human_paths:
    if len(human_annotations_dict) > 2:
        fkappa = compute_fleiss_kappa(human_annotations_dict, LABELS)
        report_lines.append('## Inter-Rater Agreement')
        report_lines.append(f"- Fleiss' Kappa (across all human annotators): {fkappa:.3f}\n")

if llm_paths:
    #*Fleiss kappa between all llms
    if len(llm_annotations_dict) > 2:
        fkappa = compute_fleiss_kappa(llm_annotations_dict, list(LABELS) + [""])
        report_lines.append(f"- Fleiss' Kappa (across all LLM annotators): {fkappa:.3f}\n")


    #*Fleiss kappa between humans within different llm-families
    for family, models_in_family in llm_families.items():
        if len(models_in_family) > 2:
            # select subset of annotations from llm_annotations_dict
            subset = {k: v for k, v in llm_annotations_dict.items() if k in models_in_family}
            fkappa = compute_fleiss_kappa(subset, list(LABELS) + [""])
            report_lines.append(f"- Fleiss' Kappa (across {family}): {fkappa:.3f}\n")

    
    #*Average Kappa between each human and each family of llm
    if human_paths:
        report_lines.append('## Human vs LLM Rater Agreement')
        report_lines.append("| Human | LLM type | Avg Agreement Rate (%) | Avg Cohen's Kappa |")
        report_lines.append("|-------|---------|---------------------|----------------|")
        for human in human_annotations_dict:
            for family, models_in_family in llm_families.items():
                # Get the kappa scores for the models in this family
                model_kappas = [rate['cohen_kappa'] for rate in agreement_rates if rate['file_B'] in models_in_family and rate['file_A'] == human]
                model_agreements = [rate['agreement_rate'] for rate in agreement_rates if rate['file_B'] in models_in_family and rate['file_A'] == human]
                if model_kappas:
                    avg_model_kappa = sum(model_kappas) / len(model_kappas)
                    avg_agreement_rate = sum(model_agreements) / len(model_agreements)
                    report_lines.append(f"| {human} | {family} (n={len(models_in_family)})| {avg_agreement_rate:.3f} | {avg_model_kappa:.3f} |")

#* report summary
report_lines.append('## Summary of Agreement Rates')
report_lines.append("| Rater 1 | Rater 2 | Agreement Rate (%) | Cohen's Kappa |")
report_lines.append("|---------|---------|---------------------|----------------|")
for rate in agreement_rates:
    report_lines.append(f"| {rate['file_A']} | {rate['file_B']} | {rate['agreement_rate']:.3f} | {rate['cohen_kappa']:.3f} |")
report_lines.append('---')

#* Summary of most confused labels and label pairs
overall_pair_keys = [
    (all_annotations_keys[i], all_annotations_keys[j])
    for i in range(len(all_annotations_keys))
    for j in range(i + 1, len(all_annotations_keys))
]

append_confusion_summary(
    report_lines,
    '## Summary of Most Confused Labels (Overall)',
    all_annotations,
    overall_pair_keys,
    labels_all,
    exclude_labels=exclude_analysis_labels,
    top_k=5,
    output_dir=args.output_dir if args.write_csv else None,
    csv_prefix="summary_overall"
)

human_human_pair_keys = [
    (human_keys[i], human_keys[j])
    for i in range(len(human_keys))
    for j in range(i + 1, len(human_keys))
]
append_confusion_summary(
    report_lines,
    '## Summary of Most Confused Labels (Humans vs Humans)',
    all_annotations,
    human_human_pair_keys,
    labels_all,
    exclude_labels=exclude_analysis_labels,
    top_k=5,
    output_dir=args.output_dir if args.write_csv else None,
    csv_prefix="summary_humans_vs_humans"
)

human_llm_pair_keys = [
    (human_key, llm_key)
    for human_key in human_keys
    for llm_key in llm_keys
]
append_confusion_summary(
    report_lines,
    '## Summary of Most Confused Labels (LLMs vs Humans)',
    all_annotations,
    human_llm_pair_keys,
    labels_all,
    exclude_labels=exclude_analysis_labels,
    top_k=5,
    output_dir=args.output_dir if args.write_csv else None,
    csv_prefix="summary_llms_vs_humans"
)

# Save report
os.makedirs(args.output_dir, exist_ok=True)
output_path = os.path.join(args.output_dir, "agreement_report.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"✅ Markdown report saved to: {output_path}")