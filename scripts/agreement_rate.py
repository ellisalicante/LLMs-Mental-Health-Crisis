import json
import os
import argparse
from sklearn.metrics import cohen_kappa_score, confusion_matrix
from statsmodels.stats.inter_rater import fleiss_kappa
import numpy as np
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.config import LABELS, LLM_LABEL_DIR, HUMAN_LABEL_DIR


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

args = argparser.parse_args()
human_paths = args.human_paths
human_paths = [human_paths] if isinstance(human_paths, str) else human_paths
llm_paths = args.llm_paths
llm_paths = [llm_paths] if isinstance(llm_paths, str) else llm_paths
original_path = args.original_path
report_lines = []

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
        if not set(labels_A).issubset(list(LABELS) + [""]):
            print(f"\nLabelsA: {set(labels_A)} -- LABELS: {LABELS}")
            raise ValueError(f"LabelsA in {name_A} are not a subset of defined LABELS.")
        if not set(labels_B).issubset(list(LABELS) + [""]):
            print(f"LabelsB: {set(labels_B)} in {name_B} are not a subset of defined LABELS.")
            raise ValueError(f"LabelsB in {name_B} are not a subset of defined LABELS.")
        
        agreement_rate = calculate_agreement_rate(labels_A, labels_B)
        kappa_score = cohen_kappa_score(labels_A, labels_B, labels=list(LABELS)+[""])
        
        agreement_rates.append({"file_A": name_A, "file_B": name_B,
            "agreement_rate": agreement_rate,
            "cohen_kappa": kappa_score
        })
        
        #* Print results
        report_lines.append(f"### `{name_A}` and `{name_B}`:")
        report_lines.append(f"\t* 🟩 Agreement Rate: {agreement_rate:.2f}%")
        report_lines.append(f"\t* 🧠 Cohen's Kappa: {kappa_score:.2f}") 
        

        #Calculate confusion matrix
        cm = confusion_matrix(labels_A, labels_B, labels=list(LABELS)+[""])
        report_lines.append(f"Confusion Matrix between `{name_A}` (ROWS) and `{name_B}` (COLS):")
        df = pd.DataFrame(cm,
                          index=list(LABELS)+[""], # f"{name_A}: {l}" for l in list(LABELS)+[""]]
                          columns=list(LABELS)+[""]) # [f"{name_B}: {l}" for l in list(LABELS)+[""]]
        report_lines.append(df.to_markdown())
        report_lines.append('')
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

# Save report
output_path = os.path.join('outputs',"agreement_report.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"✅ Markdown report saved to: {output_path}")