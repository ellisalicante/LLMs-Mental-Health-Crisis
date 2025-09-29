import argparse
import os
import sys
import json
from tqdm import tqdm 
import time
from openai import BadRequestError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.llm_prompting import get_response_to_input, get_llm_client
from src.config import AVAILABLE_LLMS, LLM_ANSWER_DIR
##############################

parser = argparse.ArgumentParser(description="Label conversations using LLM as a judge.")
parser.add_argument("--model", type=str, required=True, help="LLM model name to use for labeling.")
parser.add_argument("--dataset-path", type=str, required=True, help="Path to the dataset file containing conversations to label.")
parser.add_argument("--temp-path", required=False, default=None, help="Temporary file were previous results are saved. Must be specified if resuming from a previous run. Must have same entry order as dataset-path.")


args = parser.parse_args()
model_name = args.model
dataset_path = args.dataset_path
dataset_name = os.path.basename(dataset_path).replace('.json', '')
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
	output_path = os.path.join(LLM_ANSWER_DIR, f"{model_name.replace('/', '-')}-answers-{dataset_name}-{tmstp}.json")
	temp_path = os.path.join(LLM_ANSWER_DIR, f"TEMP_{model_name.replace('/', '-')}-answers-{dataset_name}-{tmstp}.json")
	print(f'Using NEW temporary path: {temp_path} - Final results in: {output_path}')

##############################

#* Load LLM client
if model_name not in AVAILABLE_LLMS:
	raise ValueError(f"Model {model_name} is not available. Choose from: {', '.join(AVAILABLE_LLMS)}")

client = get_llm_client(model_name)

#* Load dataset
with open(dataset_path, "r", encoding="utf-8") as f:
	   data = json.load(f)

#* Load temporal
if temp_path_prev:
	with open(temp_path_prev, "r", encoding="utf-8") as f:
		temp_data_prev = json.load(f)
	
	n_prev_temp = len(temp_data_prev)

	#check that order in temporal is the same as order in original
	for i, item in enumerate(temp_data_prev):
		if item['inputs'] != data[i]['inputs']:
			raise ValueError(f"Order mismatch at index {i}: {item['inputs']} != {data[i]['inputs']}")

##############################
#* LLM answers
errors_count = 0

for idx, item in enumerate(progress_label := tqdm(data, desc="Progress")):

	if temp_path_prev and idx < n_prev_temp and item['inputs'] == temp_data_prev[idx]['inputs']:
		print(f'input {idx} already processed, skipping...')
		item.update(temp_data_prev[idx])
	
	else:
		inputs = item["inputs"]
		inputs_string = "\n".join(inputs)
		
		try:
			raw_output, response = get_response_to_input(client, model_name, inputs_string)
			
			tokens = response.usage.total_tokens
			item['tokens'] = tokens
			item['answer'] = raw_output 
			item['refusal'] = response.choices[0].message.refusal if hasattr(response.choices[0].message, 'refusal') else None
			item['annotations'] = response.choices[0].message.annotations if hasattr(response.choices[0].message, 'annotations') else None
			item['role'] = response.choices[0].message.role if hasattr(response.choices[0].message, 'role') else None

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
			progress_label.set_description(f"Labeling Progress. Errors: {errors_count}")

		# Catch all other exceptions
		except Exception as e:
			errors_count += 1
			item['tokens'] = 0
			item['answer'] = {"error": str(e)}
			progress_label.set_description(f"Labeling Progress. Errors: {errors_count}")

	if idx % 10 == 0:
		with open(temp_path, "w", encoding="utf-8") as f:
			json.dump(data[:idx+1], f, ensure_ascii=False, indent=2)

with open(output_path, "w", encoding="utf-8") as f:
	json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Finished. Output file: {output_path}")
print(f"Total errors: {errors_count}")