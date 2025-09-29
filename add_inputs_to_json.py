
import os
import json

file_path = r"data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json"
original_path = r"data\processed\sampled_dataset_n_200_merged_n50-noSeed_156-s42.json"

with open(os.path.join(original_path), "r", encoding="utf-8") as f:
    original_data = json.load(f)

with open(os.path.join(file_path), "r", encoding="utf-8") as f:
    llm_data = json.load(f)

for idx_sample, item in enumerate(original_data):
    if llm_data[idx_sample]["dataset_id"] != item["dataset_id"]:
        raise ValueError(f"Mismatch in inputs at index {idx_sample}. LLM annotation {llm_data[idx_sample]['dataset_id']} does not match original data.")
    
    llm_data[idx_sample]["inputs"] = item["inputs"]  # Ensure inputs are included in the result


# Save updated LLM data
with open(os.path.join(file_path), "w", encoding="utf-8") as f:
    json.dump(llm_data, f, ensure_ascii=False, indent=2)
