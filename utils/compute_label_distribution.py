import json
import glob

#all_files = glob.glob('data/llm_label/gpt-4o-mini-labeled-sampled_dataset_n_2046*.json')
#all_files = glob.glob('data/llm_label/gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json')
all_files = glob.glob('data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-merged_labels*.json')


for file_path in all_files:   
    label_distribution = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        label = item.get("label")
        if label:
            label_distribution[label] = label_distribution.get(label, 0) + 1
        else:
            label_distribution["z-unknown"] = label_distribution.get("unknown", 0) + 1

    print("# Label Distribution:")
    print(f'File: {file_path}')

    for label in sorted(label_distribution.keys()):
        count = label_distribution[label]
        print(f"\t {label}: {count} ({(count/len(data))*100:.1f}%)")