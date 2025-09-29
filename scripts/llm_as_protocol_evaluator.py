import argparse
import os
import sys
import json
from tqdm import tqdm 
import time
from openai import BadRequestError
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.llm_prompting import  get_llm_client, llm_as_answer_evaluator, extract_json_correctly
from src.config import AVAILABLE_LLMS, LLM_EVALUATOR_DIR, PROTOCOL_DIR, LABELS

##############################

parser = argparse.ArgumentParser(description="Evaluation protocol of answers conversations using LLM as a judge.")
parser.add_argument("--model", type=str, required=True, help="LLM model name to use for evaluation.")
parser.add_argument("--answered-path", type=str, required=True, help="Path to the dataset file containing LLM answers to evaluate.")
parser.add_argument("--label-path", type=str, required=True, help="Path to the dataset file containing LLM categorized inputs.")
parser.add_argument("--temp-path", required=False, default=None, help="Temporary file were previous results are saved. Must be specified if resuming from a previous run. Must have same entry order as dataset-path.")


args = parser.parse_args()
model_name = args.model
answered_path = args.answered_path
label_path = args.label_path

answers_dataset_name = os.path.basename(answered_path).replace('.json', '')
temp_path_prev = args.temp_path

# Save results to output file
if temp_path_prev:
	temp_basename = os.path.basename(temp_path_prev)[5:]
	temp_dir = os.path.dirname(temp_path_prev)
	output_path = os.path.join(temp_dir, temp_basename)
	temp_path = temp_path_prev
	print(f'Using PREVIOUS temporary path: {temp_path} - Final results in: {output_path}')
else:
	tmstp = time.strftime("%Y%m%d-%H%M%S")
	output_path = os.path.join(LLM_EVALUATOR_DIR, f"{model_name.replace('/', '-')}-evaluation_{answers_dataset_name}_{tmstp}.json")
	temp_path = os.path.join(LLM_EVALUATOR_DIR, f"TEMP_{model_name.replace('/', '-')}-evaluation_{answers_dataset_name}_{tmstp}.json")
	print(f'Using NEW temporary path: {temp_path} - Final results in: {output_path}')

##############################

#* Load LLM client
if model_name not in AVAILABLE_LLMS:
	raise ValueError(f"Model {model_name} is not available. Choose from: {', '.join(AVAILABLE_LLMS)}")

client = get_llm_client(model_name)

#* Load dataset of answers
with open(answered_path, "r", encoding="utf-8") as f:
	answered_data = json.load(f)

#* Load labels
with open(label_path, "r", encoding="utf-8") as f:
	label_data = json.load(f)

# Check same inputs in label_data and answered_data
for i, item in enumerate(label_data):
	if item['inputs'] != answered_data[i]['inputs']:
		raise ValueError(f"Order mismatch at index {i}: {item['inputs']} != {answered_data[i]['inputs']}")

#* Load temporal
if temp_path_prev:
	with open(temp_path_prev, "r", encoding="utf-8") as f:
		temp_data_prev = json.load(f)
	
	n_prev_temp = len(temp_data_prev)

	#check that order in temporal is the same as order in original
	for i, item in enumerate(temp_data_prev):
		if item['inputs'] != answered_data[i]['inputs']:
			raise ValueError(f"Order mismatch at index {i}: {item['inputs']} != {answered_data[i]['inputs']}")

#* Load protocol as pandas
protocol_df = pd.read_csv(PROTOCOL_DIR, dtype=str, index_col=0)
assert not protocol_df.empty, "Protocol DataFrame is empty"
#Assert rows are  LABELS
assert all(key in LABELS for key in protocol_df.index), f"Some rows have labels not in LABELS. {[key for key in protocol_df.index]}"
# all columns as expected
expected_cols = ['(1) Harmful / Unacceptable', '(2) Inappropriate', '(3) Partially Appropriate', '(4) Mostly Appropriate', '(5) Fully Appropriate']
assert all(col in protocol_df.columns for col in expected_cols), f"Some expected columns are missing: {set(expected_cols) - set(protocol_df.columns)}"
# rename cols for simplicity
map_cols = {col: int(col[1:2]) for col in protocol_df.columns}
protocol_df.rename(columns=map_cols, inplace=True)
##############################

#* LLM answers
errors_count = 0
    
for idx, item in enumerate(progress_label := tqdm(answered_data, desc="Progress")):

	if temp_path_prev and idx < n_prev_temp and item['inputs'] == temp_data_prev[idx]['inputs']:
		print(f'input {idx} already processed, skipping...')
		item.update(temp_data_prev[idx])
	
	else:
		dataset_id = item["dataset_id"]
		label = label_data[idx]['label']
		assert label in LABELS or label == "" or label is None, f"Label '{label}' at index {idx} not in predefined LABELS or empty."
		inputs = item["inputs"]
		llm_response = item["answer"]

		try:
			if label is None or label == "":
				item['label'] = label
				item['tokens'] = 0
				item['evaluation'] = None
				item['explanation'] = ""
			else:

				raw_output = None
				raw_output, response = llm_as_answer_evaluator(model_name, client, inputs, llm_response, protocol_df, label)
				tokens = response.usage.total_tokens
				clean_output = extract_json_correctly(raw_output)
				result = json.loads(clean_output)
				tokens = response.usage.total_tokens
				item['label'] = label
				item['tokens'] = tokens
				item['evaluation'] = result['appropriateness']
				item['explanation'] = result['explanation']


		# Catch exception OpenAI refuses to answer
		except BadRequestError as e:
			errors_count += 1
			item['tokens'] = 0
			err_data = e.response.json().get("error", {})
			item['answer'] = {}
			item['answer']['message'] = err_data.get("message", '')
			item['answer']['type'] = err_data.get("type", '')
			item['answer']['code'] = err_data.get("code", '')
			item['refusal'] = True
			progress_label.set_description(f"Evaluation Progress. Errors: {errors_count}")

		# Catch all other exceptions
		except Exception as e:
			errors_count += 1
			item['label'] = label
			item['tokens'] = 0
			item['error'] = str(e)
			if raw_output:
				item['answer'] = raw_output
			progress_label.set_description(f"Evaluation Progress. Errors: {errors_count}")

	if idx % 1 == 0:
		with open(temp_path, "w", encoding="utf-8") as f:
			json.dump(answered_data[:idx+1], f, ensure_ascii=False, indent=2)

with open(output_path, "w", encoding="utf-8") as f:
	json.dump(answered_data, f, ensure_ascii=False, indent=2)

print(f"Finished. Output file: {output_path}")
print(f"Total errors: {errors_count}")
