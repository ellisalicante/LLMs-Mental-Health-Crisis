import sys
import os
import argparse
import json
from tqdm import tqdm
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.llm_prompting import llm_as_judge, extract_json_correctly, get_llm_client
from src.config import LLM_LABEL_DIR, AVAILABLE_LLMS

argparse = argparse.ArgumentParser(description="Label conversations using LLM as a judge.")
argparse.add_argument("--model", type=str, required=True, help="LLM model name to use for labeling.")
argparse.add_argument("--dataset-path", type=str, required=True, help="Path to the dataset file containing conversations to label.")


args = argparse.parse_args()
model_name = args.model
dataset_path = args.dataset_path
dataset_name = os.path.basename(dataset_path).replace('.json', '')
tmstp = time.strftime("%Y%m%d-%H%M%S")
output_path = os.path.join(LLM_LABEL_DIR, f"{model_name.replace('/', '-')}-labeled-{dataset_name}-{tmstp}.json")
###############

#* Load LLM client
if model_name not in AVAILABLE_LLMS:
    raise ValueError(f"Model {model_name} is not available. Choose from: {', '.join(AVAILABLE_LLMS)}")

client = get_llm_client(model_name)

#* Load dataset
with open(dataset_path, "r", encoding="utf-8") as f:
       data = json.load(f)

#* LLM labelling
results = []
errors_count = 0
count = 0


for item in (progress_label := tqdm(data, desc="Labeling Progress")):
    dataset_id = item["dataset_id"]
    original_label = item.get("label", None)
    inputs = item["inputs"]


    # Use LLM model if label is missing
    tokens = 0
    try:
        raw_output, response = llm_as_judge(model_name, client, inputs, dataset_id)
        tokens = response.usage.total_tokens
        clean_output = extract_json_correctly(raw_output)
        result = json.loads(clean_output)

        # Validate that the returned inputs match the original. If not, it is discarded.
        if result["dataset_id"] != dataset_id:
            raise ValueError(f"Mismatch: model returned incorrect dataset_id. Expected {dataset_id}, got {result['dataset_id']}.")
        if "label" not in result or not result["label"]:
            raise ValueError(f"Model did not return a valid label. Got: {result.get('label', None)}")

        result["tokens"] = tokens
        result["inputs"] = inputs  # Ensure inputs are included in the result

        if original_label:
            result["original_label"] = original_label

        results.append(result)
        count += 1

    except Exception as e:
        errors_count += 1
        results.append({
            "dataset_id": dataset_id,
            "inputs": inputs,
            "label": "",
            "explanation": f"Error processing input: {str(e)}",
            "tokens": 0
        })
        progress_label.set_description(f"Labeling Progress. Errors: {errors_count}")

    if count % 10 == 0:
        temp_path = os.path.join(LLM_LABEL_DIR, f"TEMP_{model_name.replace('/', '-')}-labeled-{dataset_name}-{tmstp}.json")
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    
# Save results to output file
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Finished. Output file: {output_path}")
print(f"Total errors by mismatched label or id: {errors_count}")