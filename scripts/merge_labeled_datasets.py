import argparse
import json
import os
import sys
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import LLM_LABEL_DIR, LABELS


parser = argparse.ArgumentParser(description="Merge labeled datasets")
parser.add_argument("--input-files", nargs="+", help="Paths to the input JSON files")
parser.add_argument('--output-file', help="Path to the output JSON file")
args = parser.parse_args()

input_paths = args.input_files
output_path = os.path.join(LLM_LABEL_DIR, args.output_file)

merged_data = {os.path.basename(input_file): None for input_file in input_paths}

for input_file in input_paths:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)     
        merged_data[os.path.basename(input_file)] = data    

print(merged_data.keys())
if not os.path.exists(os.path.dirname(output_path)):
    os.makedirs(os.path.dirname(output_path))


# assert merged_data size is the same for all of them
if not all(len(merged_data[key]) == len(merged_data[list(merged_data.keys())[0]]) for key in merged_data):
    raise ValueError("Merged data size is not the same for all input files.")
else:
    print(f"Merged data size is the same for all input files. Size: {len(merged_data[list(merged_data.keys())[0]])}")

final_merged = []
for idx in range(len(merged_data[list(merged_data.keys())[0]])):
    #assert the entry is the same in all files
    if not all(merged_data[key][idx]['inputs'] == merged_data[list(merged_data.keys())[0]][idx]['inputs'] for key in merged_data):
        raise ValueError(f"Entry {idx} is not the same in all files.")
    if not all(merged_data[key][idx]['dataset_id'] == merged_data[list(merged_data.keys())[0]][idx]['dataset_id'] for key in merged_data):
        raise ValueError(f"Entry {idx} is not the same in all files.")

    final_merged.append({})
    final_merged[idx]["inputs"] = merged_data[list(merged_data.keys())[0]][idx]['inputs']
    final_merged[idx]["dataset_id"] = merged_data[list(merged_data.keys())[0]][idx]['dataset_id']

    if 'original_label' in merged_data[list(merged_data.keys())[0]][idx]:
        final_merged[idx]["original_label"] = merged_data[list(merged_data.keys())[0]][idx]['original_label']

    final_merged[idx]["all_labels"] = [merged_data[key][idx]['label'] for key in merged_data]
    #assert all_labels in LABELS
    assert set(final_merged[idx]["all_labels"]).issubset(list(LABELS)+['']), f"Labels {final_merged[idx]['all_labels']} not in LABELS {LABELS}"

    #get mode of all_labels
    all_labels = final_merged[idx]["all_labels"]

    if all_labels:
        filtered_labels = [label for label in all_labels if label in LABELS]
        most_common = Counter(filtered_labels).most_common()
        if len(most_common) == 1 or (len(most_common) > 1 and most_common[0][1] > most_common[1][1]):
            final_merged[idx]["label"] = most_common[0][0]
        else:
            final_merged[idx]["label"] = None
    else:
        raise ValueError(f"No labels for entry {idx}")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(final_merged, f, ensure_ascii=False, indent=2)
