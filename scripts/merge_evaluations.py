import os
import glob
import json
import numpy as np
from tqdm import tqdm
import argparse
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

argparse = argparse.ArgumentParser(description="Label conversations using LLM as a judge.")
argparse.add_argument("--folder", type=str, required=True, help="Folder containing JSON files to merge. Dynamic comprobations will be made to only merge those with same rater, and answer dataset")

args = argparse.parse_args()

folder = args.folder# os.path.join('data', 'llm_evaluator', 'n_2000')
files = glob.glob(os.path.join(folder, '*.json'))

same_answers_files = {}

for f in files:
    evaluator = os.path.basename(f).split('_')[0]
    responder = os.path.basename(f).split('_')[1]
    responses_datasets = '_'.join(os.path.basename(f).split('_')[2:-1])
    eval_tmsp = os.path.basename(f).split('_')[-1]
    same_answers_files.setdefault(f"{responder}_{responses_datasets}", []).append(f)

# For same responder dataset --> merge evaluations
results = {}
desc='\n'
for key, files in (pbar := tqdm(same_answers_files.items(), desc=desc)):
    evaluators = [ os.path.basename(f).split('_')[0] for f in files ]
    responders = [ os.path.basename(f).split('_')[1] for f in files ]
    responsess_datasets = [ '_'.join(os.path.basename(f).split('_')[2:-1]) for f in files ]
    eval_tmsps = [ os.path.basename(f).split('_')[-1] for f in files ]
    assert len(set(evaluators)) == 1, "Only can merge evaluations from same evaluator"
    assert len(set(responders)) == 1, "Only can merge evaluations from same responder"
    assert len(set(responsess_datasets)) == 1, "Only can merge evaluations from same responses dataset"
    assert len(set(eval_tmsps)) == len(files), "All timestamps of evaluations must be unique"

    

    result = []

    merged_data = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
            merged_data.append(data)

    assert len(set([len(d) for d in merged_data])) == 1, "Inconsistent merged data lengths"

    # Go through all the examples
    for input_idx in range(len(merged_data[0])):

        #check all the inputs are the same
        assert len(set([' ' .join(merged_data[eval_idx][input_idx]['inputs']) for eval_idx in range(len(merged_data))]))==1

        result.append(merged_data[0][input_idx])

        # Remove unnecessary fields
        if 'tokens' in result[input_idx]:
            del result[input_idx]['tokens']
        if 'annotations' in result[input_idx]:
            del result[input_idx]['annotations']
        if 'role' in result[input_idx]:
            del result[input_idx]['role']
        
        # Gather all evaluations
        evals = [merged_data[eval_idx][input_idx]['evaluation'] for eval_idx in range(len(merged_data)) if 'evaluation' in merged_data[eval_idx][input_idx]]
        # safely convert each eval to int
        evals = [int(eval) if eval is not None else None for eval in evals]
        result[input_idx]['evals'] = evals
        
        if all(eval == None for eval in evals):
            result[input_idx]['evaluation'] = None
        else:
            eval_filter = [eval for eval in evals if eval is not None]
            result[input_idx]['evaluation'] = np.mean(eval_filter).item()
            result[input_idx]['evaluation_std'] = np.std(eval_filter).item() if len(eval_filter) > 1 else 0.0
    

    output_path = os.path.join(folder, 'merged')
    output_file = os.path.join(output_path,f"{evaluators[0]}_{responders[0]}_{responsess_datasets[0]}_merged.json")
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, indent=2, ensure_ascii=False)
        print(f"Merged {len(files)} evaluations into {output_file} with {len(result)} entries.\n")
        