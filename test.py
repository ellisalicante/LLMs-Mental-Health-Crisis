import json

file1 = r'data\processed\merged_dataset_all.json'

with open(file1, 'r', encoding='utf-8') as f1:
    data1 = json.load(f1)

# track seen "inputs" across all datasets
seen = set()
cleaned_data = []

for dataset in data1:
    new_dataset = {
        "dataset_id": dataset['dataset_id'],
        "content": []
        }
    for item in dataset['content']:
        # turn the list of inputs into a tuple so it's hashable
        key = tuple(item['inputs'])
        if key not in seen:
            seen.add(key)
            new_dataset["content"].append(item)
    # only keep dataset if it has any content left
    if new_dataset["content"]:
        cleaned_data.append(new_dataset)
    else:
        print(f"Dataset {dataset['dataset_id']} is empty after deduplication.")

# save back
with open(r'data\processed\merged_dataset_unique.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)
print(f"Original number of datasets: {len(data1)}")
print(f"Number of unique datasets: {len(cleaned_data)}")
