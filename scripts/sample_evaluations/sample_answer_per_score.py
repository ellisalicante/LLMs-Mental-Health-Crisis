import os
import glob
import json
import numpy as np
from tqdm import tqdm
import argparse
import sys
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


parser = argparse.ArgumentParser(description="Sample conversation answers based on the gpt-4o-mini evaluation score.")
parser.add_argument('--input_dir', type=str, default='../../data/llm_evaluator/gpt-4o-mini/n_200/merged',
                    help='Directory containing the merged evaluation files')
parser.add_argument('--output_dir', type=str, default='../../data/llm_evaluator/sampled',
                    help='Directory to save the sampled dataset')
parser.add_argument('--output_name', type=str, default=None,
                    help='Name of the output file (without extension). If not provided, will use timestamp.')
parser.add_argument('--criteria', type=str, default='highest', choices=['highest', 'lowest', 'median', 'random'],
                    help='Criteria for selecting the answer: highest, lowest, median, or random score')

""" 
Goal: Sample 200 conversations from the validation test.
Description: From the dataset of 200 user inputs, we have 3 answers per model and 5 models, thus, 15 answers per user input. 
They are evaluated by gpt-4o-mini in `data\llm_evaluator\gpt-4o-mini\n_200\merged`. Each file contains the 200 userInputs-answer 
for a model and iteration. We need to sample one answer for each user input based on some criteria on the gpt-4o-mini score. 
Thus, for each user input, we will select the answer with the highest score. A new dataset will be created with the sampled answers.
"""


def load_all_evaluations(input_dir):
    """
    Load all evaluation JSON files from the specified directory.
    
    Returns:
        list: List of tuples (filename, data) for each JSON file
    """
    json_files = glob.glob(os.path.join(input_dir, '*.json'))
    
    if not json_files:
        raise ValueError(f"No JSON files found in {input_dir}")
    
    print(f"Found {len(json_files)} evaluation files")
    
    all_data = []
    for json_file in tqdm(json_files, desc="Loading evaluation files"):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_data.append((os.path.basename(json_file), data))
    
    return all_data


def verify_consistency(all_data):
    """
    Verify that all files have the same number of entries and that inputs are consistent across files.
    
    Returns:
        int: Number of user inputs
    """
    if not all_data:
        raise ValueError("No data to verify")
    
    # Check number of entries
    num_entries = len(all_data[0][1])
    print(f"\nVerifying consistency across {len(all_data)} files...")
    print(f"Expected number of entries per file: {num_entries}")
    
    for filename, data in all_data:
        if len(data) != num_entries:
            raise ValueError(f"File {filename} has {len(data)} entries, expected {num_entries}")
    
    # Verify that inputs are in the same order across all files
    reference_inputs = [entry['inputs'] for entry in all_data[0][1]]
    reference_dataset_ids = [entry['dataset_id'] for entry in all_data[0][1]]
    
    for filename, data in all_data[1:]:
        current_inputs = [entry['inputs'] for entry in data]
        current_dataset_ids = [entry['dataset_id'] for entry in data]
        
        if current_dataset_ids != reference_dataset_ids:
            raise ValueError(f"File {filename} has different dataset_ids order than reference file")
        
        # Additional check: verify inputs match
        for i, (ref_inp, curr_inp) in enumerate(zip(reference_inputs, current_inputs)):
            if ref_inp != curr_inp:
                raise ValueError(f"File {filename} has different inputs at index {i}")
    
    print(f"✓ All files are consistent with {num_entries} entries each")
    return num_entries


def sample_answers_by_criteria(all_data, criteria='highest'):
    """
    Sample one answer per user input based on the specified criteria.
    
    Args:
        all_data: List of tuples (filename, data)
        criteria: 'highest', 'lowest', 'median', or 'random'
    
    Returns:
        list: Sampled dataset with one answer per user input
    """
    num_inputs = len(all_data[0][1])
    sampled_dataset = []
    all_null_count = 0
    
    print(f"\nSampling answers using '{criteria}' criteria...")
    
    for i in tqdm(range(num_inputs), desc="Sampling answers"):
        # Collect all answers for this user input
        candidates = []
        candidates_with_scores = []
        for filename, data in all_data:
            entry = data[i]
            eval_score = entry['evaluation']
            candidates.append({
                'source_file': filename,
                'evaluation': eval_score,
                'entry': entry
            })
            # Track candidates that have non-null evaluations separately
            if eval_score is not None:
                candidates_with_scores.append({
                    'source_file': filename,
                    'evaluation': eval_score,
                    'entry': entry
                })
        
        # If we have non-null evaluations, use only those; otherwise use all candidates
        if candidates_with_scores:
            selection_pool = candidates_with_scores
        else:
            # All evaluations are null - just pick the first one
            selection_pool = candidates
            all_null_count += 1
        
        # Select based on criteria
        if criteria == 'highest':
            selected = max(selection_pool, key=lambda x: x['evaluation'] if x['evaluation'] is not None else float('-inf'))
        elif criteria == 'lowest':
            selected = min(selection_pool, key=lambda x: x['evaluation'] if x['evaluation'] is not None else float('inf'))
        elif criteria == 'median':
            sorted_candidates = sorted(selection_pool, key=lambda x: x['evaluation'] if x['evaluation'] is not None else float('-inf'))
            selected = sorted_candidates[len(sorted_candidates) // 2]
        elif criteria == 'random':
            selected = selection_pool[np.random.randint(len(selection_pool))]
        else:
            raise ValueError(f"Unknown criteria: {criteria}")
        
        # Add source information to the selected entry
        sampled_entry = selected['entry'].copy()
        sampled_entry['sampled_from'] = selected['source_file']
        sampled_entry['sampled_criteria'] = criteria
        
        sampled_dataset.append(sampled_entry)
    
    if all_null_count > 0:
        print(f"⚠ Warning: {all_null_count} entries had all null evaluations across all 15 files")
    
    return sampled_dataset


def save_sampled_dataset(sampled_dataset, output_dir, output_name=None):
    """
    Save the sampled dataset to a JSON file.
    
    Args:
        sampled_dataset: List of sampled entries
        output_dir: Directory to save the file
        output_name: Name of the output file (without extension)
    
    Returns:
        str: Path to the saved file
    """
    os.makedirs(output_dir, exist_ok=True)
    
    if output_name is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_name = f"sampled_dataset_{timestamp}"
    
    output_path = os.path.join(output_dir, f"{output_name}.json")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sampled_dataset, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Sampled dataset saved to: {output_path}")
    return output_path


def print_statistics(sampled_dataset):
    """
    Print statistics about the sampled dataset.
    """
    print("\n" + "="*60)
    print("SAMPLING STATISTICS")
    print("="*60)
    
    # Separate entries with null evaluations from those with actual scores
    scores = [entry['evaluation'] for entry in sampled_dataset if entry['evaluation'] is not None]
    null_count = sum(1 for entry in sampled_dataset if entry['evaluation'] is None)
    
    print(f"Total sampled entries: {len(sampled_dataset)}")
    print(f"Entries with null evaluation: {null_count}")
    
    if scores:
        print(f"\nScore distribution (for {len(scores)} non-null entries):")
        print(f"  Mean:   {np.mean(scores):.3f}")
        print(f"  Median: {np.median(scores):.3f}")
        print(f"  Std:    {np.std(scores):.3f}")
        print(f"  Min:    {np.min(scores):.3f}")
        print(f"  Max:    {np.max(scores):.3f}")
        
        # Count by score
        from collections import Counter
        score_counts = Counter(scores)
        print(f"\nScore counts:")
        for score in sorted(score_counts.keys()):
            print(f"  Score {score}: {score_counts[score]} entries ({score_counts[score]/len(scores)*100:.1f}%)")
    else:
        print(f"\nNo entries with non-null evaluations")
    
    # Source file distribution
    source_files = [entry['sampled_from'] for entry in sampled_dataset]
    source_counts = Counter(source_files)
    print(f"\nTop 5 source files:")
    for source_file, count in source_counts.most_common(5):
        # Shorten filename for display
        short_name = source_file[:60] + '...' if len(source_file) > 60 else source_file
        print(f"  {short_name}: {count} entries")
    
    print("="*60)


def main():
    args = parser.parse_args()
    
    print("="*60)
    print("SAMPLING ANSWERS BY EVALUATION SCORE")
    print("="*60)
    print(f"Input directory: {args.input_dir}")
    print(f"Output directory: {args.output_dir}")
    print(f"Selection criteria: {args.criteria}")
    print("="*60)
    
    # Load all evaluation files
    all_data = load_all_evaluations(args.input_dir)
    
    # Verify consistency
    num_inputs = verify_consistency(all_data)
    
    # Sample answers
    sampled_dataset = sample_answers_by_criteria(all_data, criteria=args.criteria)
    
    # Print statistics
    print_statistics(sampled_dataset)
    
    # Save sampled dataset
    output_path = save_sampled_dataset(sampled_dataset, args.output_dir, args.output_name)
    
    print(f"\n✓ Done! Sampled {len(sampled_dataset)} conversations")


if __name__ == "__main__":
    main()



