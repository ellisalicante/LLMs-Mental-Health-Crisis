import json
import glob
import os
from collections import defaultdict

input_dir = '../../data/llm_evaluator/gpt-4o-mini/n_200/merged'
json_files = sorted(glob.glob(os.path.join(input_dir, '*.json')))

print(f"Found {len(json_files)} files\n")

# Load all files
all_data = []
for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_data.append((os.path.basename(json_file), data))

# Check for entries where all evaluations are null
num_inputs = len(all_data[0][1])
all_null_entries = []
partially_null_entries = defaultdict(list)

for i in range(num_inputs):
    evaluations = []
    for filename, data in all_data:
        eval_val = data[i]['evaluation']
        evaluations.append(eval_val)
    
    null_count = sum(1 for e in evaluations if e is None)
    
    if null_count == len(evaluations):  # All 15 are null
        all_null_entries.append(i)
    elif null_count > 0:  # Some are null
        partially_null_entries[i] = null_count

print(f"Entries with ALL 15 evaluations null: {len(all_null_entries)}")
if all_null_entries:
    print(f"Indices: {all_null_entries[:5]}...")

print(f"\nEntries with SOME null evaluations: {len(partially_null_entries)}")
if partially_null_entries:
    print(f"Sample (index: count of nulls):")
    for idx, count in list(partially_null_entries.items())[:10]:
        print(f"  Index {idx}: {count} nulls out of 15")
        # Show the evaluations for this entry
        evals = [all_data[j][1][idx]['evaluation'] for j in range(len(all_data))]
        print(f"    Evaluations: {evals}")
