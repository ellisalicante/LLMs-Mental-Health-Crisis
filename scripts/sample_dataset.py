import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
import json
import argparse
from src.config import CUSTOM_SAMPLE_SIZES, DEFAULT_N, DEFAULT_SEED, MERGED_DATASET_DIR, SAMPLED_DATASET_DIR


argparser = argparse.ArgumentParser(description="Load and save datasets.")
argparser.add_argument('--seed', type=int, default=DEFAULT_SEED, help='Random seed for reproducibility.')
argparser.add_argument('--n', type=int, default=DEFAULT_N, help='Number of conversations to sample from each dataset.')
args = argparser.parse_args()

random.seed(args.seed)  # For reproducibility
N_SAMPLE = args.n

merged_all_path = os.path.join(MERGED_DATASET_DIR, "merged_dataset_all.json")

sampled_merged = []

if os.path.exists(merged_all_path):
    with open(merged_all_path, "r", encoding="utf-8") as f:
        merged_data = json.load(f)

    for dataset_json in merged_data:
        dataset_id = dataset_json["dataset_id"]
        content = dataset_json["content"]

        # Sample conversations
        n = CUSTOM_SAMPLE_SIZES.get(dataset_id, N_SAMPLE)
        print(f"\tSampling {min(n, len(content))} conversations from {dataset_id}...")
        sampled = random.sample(content, min(n, len(content)))  
        # add dataset_id to each conversation
        for conversation in sampled:
            conversation["dataset_id"] = dataset_id
            sampled_merged.append(conversation)
        
        #sampled_merged.extend(random.sample(content, min(n, len(content))))
        #sampled_merged.append({
        #    "dataset_id": dataset_id,
        #    "content": sampled
        #})

    # Save file
    sampled_path = os.path.join(SAMPLED_DATASET_DIR, f"sampled_dataset_n_{len(sampled_merged)}_nPerD{N_SAMPLE}_seed{args.seed}.json")
    with open(sampled_path, "w", encoding="utf-8") as f:
        json.dump(sampled_merged, f, ensure_ascii=False, indent=2)

else:
    raise FileNotFoundError(f"Merged dataset not found. Please run the script to create it. Expected path: {merged_all_path}")


#* Print summary of the merged data
print("\n#### Summary of merged data:")


total_conversations_with_labels = len([conv for conv in sampled_merged if conv.get("label") not in [None, ""]])
total_interventions = sum(len(conv["inputs"]) for conv in sampled_merged)

print(f"Number of datasets processed: {len(merged_data)}")
print(f"Total number of conversations: {len(sampled_merged)}") 
print(f"\tTotal number of conversations with labels: {total_conversations_with_labels}")
print(f"Total number of interventions: {total_interventions}")