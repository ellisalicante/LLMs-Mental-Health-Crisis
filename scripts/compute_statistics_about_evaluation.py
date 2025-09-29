import json
import os
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Merge labeled datasets")
parser.add_argument("--input-files", nargs="+", help="Paths to the input JSON files")

args = parser.parse_args()
files = args.input_files
assert len(files) > 0, "Need at least one file to compute statistics"

evaluators = [ os.path.basename(f).split('_')[0] for f in files ]
responders = [ os.path.basename(f).split('_')[1] for f in files ]
responsess_datasets = [ '_'.join(os.path.basename(f).split('_')[2:-1]) for f in files ]

assert len(set(evaluators)) == 1, "Only can merge evaluations from same evaluator"
assert len(set(responders)) == 1, "Only can merge evaluations from same responder"
assert len(set(responsess_datasets)) == len(files), "Different response from the same responder are needed"

merged_data = []

merged_evaluations = []
merged_stds = []

print("# Individual file analysis")
print (r"File & Num examples & Mean Std devs & Mean Evaluations & 1 & \leq 2.3 & \leq 3.6  & \geq 3.6")
for f in files:
    stds = []
    evaluations = []
    with open(f, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        merged_data.append(data)
    
    for input_example in data:
        if 'evaluation' in input_example and input_example['evaluation'] is not None:
            stds.append(input_example['evaluation_std'])
            evaluations.append(input_example['evaluation'])
    evaluations = np.array(evaluations)
    stds = np.array(stds)
    merged_evaluations.append(evaluations)
    merged_stds.append(stds)
    #values, counts = np.unique(evaluations, return_counts=True)
    #percentages = counts / counts.sum() * 100
    #for v, p in zip(values, percentages):
    #    print(f"Val {v:.2f}: {p:.2f}%", end='-')
    #print()

    responder = os.path.basename(f).split('_')[1]
    responses_datasets = '_'.join(os.path.basename(f).split('_')[2:-1])

    row = (
    f"{responder}-{responses_datasets} & "
    f"{len(data)} & "
    f"{np.mean(stds):.4f} & "
    f"{np.mean(evaluations):.4f} & "
    f"{(np.sum(evaluations == 1) / evaluations.size) * 100:.2f}\\% & "
    f"{(np.sum(evaluations <= 2.3333) / evaluations.size) * 100:.2f}\\% & "
    f"{(np.sum(evaluations <= 3.66666) / evaluations.size) * 100:.2f}\\% &"
    f"{(np.sum(evaluations > 3.66666) / evaluations.size) * 100:.2f}\\% \\\\"
    )
    print(row)

assert len(set([len(d) for d in merged_data])) == 1, "Inconsistent merged data lengths"

print("# Together file analysis")

merged_evaluations = np.concatenate(merged_evaluations)
merged_stds = np.concatenate(merged_stds)

print(f"{responders[0]} & {len(merged_evaluations)} & {np.mean(merged_stds):.4f} & {np.mean(merged_evaluations):.4f} & "
      f"{(np.sum(merged_evaluations == 1) / merged_evaluations.size) * 100:.2f}\\% & "
      f"{(np.sum(merged_evaluations <= 2.33333) / merged_evaluations.size) * 100:.2f}\\% & "
      f"{(np.sum(merged_evaluations <= 3.66666) / merged_evaluations.size) * 100:.2f}\\% &"
      f"{(np.sum(merged_evaluations > 3.66666) / merged_evaluations.size) * 100:.2f}\\% \\\\"
)
