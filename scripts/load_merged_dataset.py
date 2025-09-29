import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src.load_datasets as dt
from src.config import AVAILABLE_DATASETS, IND_DATASETS_DIR, MERGED_DATASET_DIR
from src.preprocessing_datasets import clean_sentence

import argparse
import json


parser = argparse.ArgumentParser(description="Load and save datasets.")
parser.add_argument('--datasets', nargs='+', required=False, default=None,
                    help='List of datasets to load and save.')
parser.add_argument('--force-download', action='store_true',
                    help='Force download of datasets even if they already exist.')
parser.add_argument('--force-merge', action='store_true',
                    help='Force merging of datasets even if merged dataset already exists.')
# Parse the command line arguments
args = parser.parse_args()
download_datasets = args.force_download
force_merge = args.force_merge

# create directories if they do not exist
if not os.path.exists(IND_DATASETS_DIR):
    os.makedirs(IND_DATASETS_DIR)
if not os.path.exists(MERGED_DATASET_DIR):
    os.makedirs(MERGED_DATASET_DIR)


#* Determine which datasets to load based on command line arguments
if args.datasets is None:
    datasets = AVAILABLE_DATASETS
else:
    datasets = [x for x in AVAILABLE_DATASETS if x in args.datasets]
    not_available = set(args.datasets) - set(datasets)
    if not_available:
        print(f"Warning: The following datasets are not available: {', '.join(not_available)}")


#* Load and save the datasets
fail = []
print(f"#### Loading datasets... {datasets}")
for dataset in datasets:
    print(f"Loading {dataset}...")
    try:
        #check if the dataset is already loaded ({dataset}.json exists under IND_DATASETS_DIR)
        dataset_path = os.path.join(IND_DATASETS_DIR, f"{dataset}.json")
        if os.path.exists(dataset_path) and not download_datasets:
            print(f"\tDataset {dataset} already exists. Skipping loading.")
        else:
            dt.load_and_save_dataset(dataset)

    except Exception as e:
        print(f"\tError loading {dataset}: {e}")
        fail.append(dataset)


#* Merge json from all the datasets - WE SAMPLE INSTANCES
merged_data = []

print("#### Merging datasets...")
#Check if merged dataset exists, if so, load it 
if os.path.exists(os.path.join(MERGED_DATASET_DIR, "merged_dataset_all.json")) and not force_merge:
    print(f"\tMerged dataset already exists at {os.path.join(MERGED_DATASET_DIR, 'merged_dataset_all.json')}. Loading existing data.")
    with open(os.path.join(MERGED_DATASET_DIR, "merged_dataset_all.json"), "r", encoding="utf-8") as f:
        merged_data = json.load(f)
else:
    for dataset_id in datasets:
        print(f"Processing {dataset_id}...")

        if dataset_id in fail:
            print(f"\tSkipping {dataset_id} due to previous loading error.")
            continue

        with open(os.path.join(IND_DATASETS_DIR, f"{dataset_id}.json"), "r", encoding="utf-8") as f:
            content = json.load(f)

        cleaned_content = []
        print(f"\tCleaning sentences in {dataset_id}...")
        for entry in content:
            # Apply again clean_sentence() and remove Nones #!WHY AGAIN?
            cleaned_inputs = [clean_sentence(s) for s in entry["inputs"]]
            cleaned_inputs = [s for s in cleaned_inputs if s]

            # Eliminate conversation if after cleaning it is None
            if not cleaned_inputs:
                continue

            cleaned_content.append({
                "inputs": cleaned_inputs,
                "label": entry.get("label", "")
            })

        # Remove duplicates within each dataset (by inputs)
        cleaned_content = list({tuple(entry["inputs"]): entry for entry in cleaned_content}.values())

        # Merge all content
        merged_data.append({
            "dataset_id": dataset_id,
            "content": cleaned_content
        })

    # Save file
    merged_path = os.path.join(MERGED_DATASET_DIR,f"merged_dataset_all.json")
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"Done. Merged data saved to {merged_path}")
    print(f"Failed to load datasets: {fail}") if fail else print("All datasets loaded successfully.")



#* Print summary of the merged data
print("\n#### Summary of merged data:")

total_conversations = sum(len(dataset["content"]) for dataset in merged_data)
total_conversations_with_labels = sum(
    len([entry for entry in dataset["content"] if entry.get("label") not in [None, ""]])
    for dataset in merged_data
)
total_interventions = sum(len(entry["inputs"]) for dataset in merged_data for entry in dataset["content"])

print(f"Number of datasets processed: {len(merged_data)}")
print(f"Total number of conversations: {total_conversations}") 
print(f"\tTotal number of conversations with labels: {total_conversations_with_labels}")
print(f"Total number of interventions: {total_interventions}")