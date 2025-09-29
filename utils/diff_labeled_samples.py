import json
import os


file1 = r"data\human_label\AA_labeled_n50.json"
file2 = r"data\human_label\ED_labeled_n50.json"


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)  
    
def compare_json_files(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)

    if len(data1) != len(data2):
        print(f"Files have different number of entries: {len(data1)} vs {len(data2)}")
        return

    for i in range(len(data1)):
        if data1[i]['inputs'] != data2[i]['inputs']:
            raise ValueError(f"Input mismatch at index {i}: {data1[i]['inputs']} vs {data2[i]['inputs']}")
        else:
            if data1[i]['label'] != data2[i]['label']:
                print('-' * 20)
                print(data1[i]['inputs'])
                print(f"AA: {data1[i]['label']}")
                print(f"ED: {data2[i]['label']}")
                print()


if __name__ == "__main__":
    compare_json_files(file1, file2)
    print("Comparison completed successfully.")