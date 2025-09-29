import json

# r'data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json'
# r'data\processed\sampled_dataset_n_2046_nPerD168_seed0.json'
# data\processed\merged_dataset_all.json
file1 = r'data\processed\merged_dataset_all.json'
file2 = None

with open(file1, 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)

inputs1 = set(tuple(obj['inputs']) for obj in data1 if 'inputs' in obj)

if file2:
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    inputs2 = set(tuple(obj['inputs']) for obj in data2 if 'inputs' in obj)

    duplicates = inputs1 & inputs2
    print(f"Number of duplicated entries between 2 files: {len(duplicates)}")
    print(len(data1), len(inputs1))
    print(len(data2), len(inputs2))

    duplicates2 = len(data2) - len(inputs2)
    print(f"Number of duplicated entries within file 2: {duplicates2}")

    total_unique = inputs1 | inputs2
    print(f"Total unique entries across both files: {len(total_unique)}")
else:
    print(len(data1), len(inputs1))
    duplicates2 = 0

duplicates1 = len(data1) - len(inputs1)
print(f"Number of duplicated entries within file 1: {duplicates1}")
if not file2:
    print("File 2 not provided; skipping cross-file duplicate checks.")
