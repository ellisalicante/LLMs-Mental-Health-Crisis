import json
from collections import Counter

# Load the sampled dataset
with open(r'..\..\data\llm_evaluator\sampled\sampled_best_answers_n200.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check dataset_ids
dataset_ids = [entry['dataset_id'] for entry in data]
print(f'Total entries: {len(dataset_ids)}')
print(f'Unique dataset_ids: {len(set(dataset_ids))}')

# Check for duplicates
counts = Counter(dataset_ids)
duplicates = {k: v for k, v in counts.items() if v > 1}
print(f'Duplicates: {len(duplicates)}')

if duplicates:
    print('Duplicate IDs:', list(duplicates.items())[:5])
else:
    print('No duplicates found - each user input appears exactly once!')

# Check scores
scores = [entry['evaluation'] if entry['evaluation'] is not None else 0 for entry in data]
score_counts = Counter(scores)
print(f'\nScore distribution:')
for score in sorted(score_counts.keys()):
    print(f'  Score {score}: {score_counts[score]} entries ({score_counts[score]/len(scores)*100:.1f}%)')
