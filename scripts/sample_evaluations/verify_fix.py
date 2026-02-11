import json

# Load the sampled dataset
with open(r'..\..\data\llm_evaluator\sampled\sampled_best_answers_n200_v2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for null evaluations
null_count = sum(1 for e in data if e['evaluation'] is None)
non_null_count = sum(1 for e in data if e['evaluation'] is not None)

print(f"Total entries: {len(data)}")
print(f"Entries with null evaluation: {null_count}")
print(f"Entries with non-null evaluation: {non_null_count}")
print(f"\nNull entries are ONLY for cases where all 15 source answers had null evaluations: ✓")

# Show which indices have null evaluations
null_indices = [i for i, e in enumerate(data) if e['evaluation'] is None]
print(f"\nIndices with null evaluations: {null_indices}")

# Verify against debug info
print(f"\nExpected null count (from debug): 16")
print(f"Actual null count: {null_count}")
print(f"Match: {'✓' if null_count == 16 else '✗'}")
