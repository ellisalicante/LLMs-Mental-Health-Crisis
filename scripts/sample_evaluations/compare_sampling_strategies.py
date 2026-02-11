import json
import os
from collections import Counter
import numpy as np

# Load all 4 sampled datasets
datasets = {
    'highest': '../../data/llm_evaluator/sampled/sampled_best_answers_n200_v2.json',
    'lowest': '../../data/llm_evaluator/sampled/sampled_lowest_scores_n200.json',
    'median': '../../data/llm_evaluator/sampled/sampled_median_scores_n200.json',
    'random': '../../data/llm_evaluator/sampled/sampled_random_scores_n200.json',
}

print("="*80)
print("COMPARISON OF SAMPLING STRATEGIES")
print("="*80)

results = {}

for strategy, filepath in datasets.items():
    if not os.path.exists(filepath):
        print(f"⚠ File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get scores
    scores = [e['evaluation'] for e in data if e['evaluation'] is not None]
    null_count = sum(1 for e in data if e['evaluation'] is None)
    
    results[strategy] = {
        'total': len(data),
        'null_count': null_count,
        'non_null_count': len(scores),
        'scores': scores
    }
    
    # Calculate statistics
    mean_score = np.mean(scores) if scores else 0
    median_score = np.median(scores) if scores else 0
    std_score = np.std(scores) if scores else 0
    min_score = np.min(scores) if scores else 0
    max_score = np.max(scores) if scores else 0
    
    print(f"\n{strategy.upper()} STRATEGY")
    print("-" * 80)
    print(f"Total entries: {len(data)}")
    print(f"Entries with null evaluation: {null_count}")
    print(f"Entries with scores: {len(scores)}")
    print(f"\nStatistics (for {len(scores)} non-null entries):")
    print(f"  Mean:   {mean_score:.4f}")
    print(f"  Median: {median_score:.4f}")
    print(f"  Std:    {std_score:.4f}")
    print(f"  Min:    {min_score:.4f}")
    print(f"  Max:    {max_score:.4f}")
    
    # Score distribution
    score_counts = Counter(scores)
    print(f"\nScore Distribution:")
    for score in sorted(score_counts.keys()):
        count = score_counts[score]
        pct = (count / len(scores)) * 100
        bar_length = int(pct / 2)  # Scale for display
        bar = '█' * bar_length
        print(f"  Score {score:>5.2f}: {count:>3} entries ({pct:>5.1f}%) {bar}")

# Create summary comparison table
print("\n" + "="*80)
print("SUMMARY COMPARISON TABLE - STATISTICS")
print("="*80)

print(f"\n{'Strategy':<12} {'Total':<8} {'Nulls':<8} {'Mean':<10} {'Median':<10} {'Std':<10} {'Min':<10} {'Max':<10}")
print("-" * 80)

for strategy in ['highest', 'lowest', 'median', 'random']:
    if strategy in results:
        r = results[strategy]
        scores = r['scores']
        mean_score = np.mean(scores) if scores else 0
        median_score = np.median(scores) if scores else 0
        std_score = np.std(scores) if scores else 0
        min_score = np.min(scores) if scores else 0
        max_score = np.max(scores) if scores else 0
        
        print(f"{strategy:<12} {r['total']:<8} {r['null_count']:<8} {mean_score:<10.4f} {median_score:<10.4f} {std_score:<10.4f} {min_score:<10.4f} {max_score:<10.4f}")

# Score range comparison table
print("\n" + "="*80)
print("SCORE RANGE DISTRIBUTION TABLE")
print("="*80)

# Define score ranges
ranges = [
    (1.0, 2.0, "1.0-2.0"),
    (2.0, 3.0, "2.0-3.0"),
    (3.0, 4.0, "3.0-4.0"),
    (4.0, 5.0, "4.0-5.0"),
]

# Calculate counts for each range and strategy
range_data = {}
for strategy in ['highest', 'lowest', 'median', 'random']:
    if strategy in results:
        range_data[strategy] = {}
        scores = results[strategy]['scores']
        total = len(scores)
        
        for min_val, max_val, label in ranges:
            # Count scores in range [min_val, max_val]
            count = sum(1 for s in scores if min_val <= s <= max_val)
            pct = (count / total * 100) if total > 0 else 0
            range_data[strategy][label] = (count, pct)

# Print the table
print(f"\n{'Strategy':<12}", end="")
for _, _, label in ranges:
    print(f"{label:<20}", end="")
print()

print("-" * (12 + 20*4))

for strategy in ['highest', 'lowest', 'median', 'random']:
    print(f"{strategy:<12}", end="")
    for _, _, label in ranges:
        if strategy in range_data:
            count, pct = range_data[strategy][label]
            print(f"{count:>3} ({pct:>5.1f}%)       ", end="")
    print()

print("="*80)
