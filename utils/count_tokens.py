import json
import os
import glob
from tqdm import tqdm

files = glob.glob("data/llm_evaluator/n_200/*.json")
print(files)
total_tokens = 0
total_chars = 0
results = {k:{} for k in files}

for file in tqdm(files, desc="Processing files"):
    file_tokens = 0
    file_chars = 0
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in tqdm(data, desc=f"Counting tokens in {os.path.basename(file)}", leave=False):
            file_tokens += item.get("tokens", 0)
            file_chars += len(item.get("answer", 0))
    total_tokens += file_tokens
    total_chars += file_chars
    results[file]["tokens"] = file_tokens
    results[file]["characters"] = file_chars
    



for file in files:
    print(f" - Total tokens in {file}:\n\t{results[file]['tokens']}")
    print(f" - Total characters in {file}:\n\t{results[file]['characters']}")

print(f"Grand total tokens:\n\t{total_tokens}")
print(f"Grand total characters:\n\t{total_chars}")
