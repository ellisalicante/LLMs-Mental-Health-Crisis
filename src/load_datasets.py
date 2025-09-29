import regex as re
from datasets import load_dataset
from src.preprocessing_datasets import process_dicts_to_json, process_texts_to_json
from src.config import LABELS, SPLIT_PATTERN_1, MAX_INTERVENTIONS

def load_hugging_1():
    """https://huggingface.co/datasets/sajjadhadi/Mental-Disorder-Detection-Data"""

    # Mapping of label variants
    label_mapping = {
        "Suicide": "suicidal_ideation",
        "Anxiety": "anxiety_crisis"
    }
    remove_original_labels = True

    def extract_hugging_1(entry):
        """
        Extracts the user statement ('text') and label ('response') from an entry of the Hugging_1 dataset.

        This function looks for a specific pattern in the 'text' field:
        "The Patient statement is: ... Based on the context, the disorder may be:"
        It skips any '[deleted]' markers that may appear between the two parts.

        Args:
        entry (dict): A single dataset record with keys 'text' and 'response'.

        Returns:
        dict or None: On success, a dict with:
            - 'statement': the extracted patient statement (stripped of whitespace)
            - 'response': the original 'response' value (stripped)
        If the pattern is not found, increments a global error counter and returns None.
        """
        #global cont_error   # counter for entries where extraction fails
        text = entry['text']
        response = entry['response']
        # Search for the correct content and not including [deleted] if it appears
        text_patron = r"The Patient statement is:(.*?)(?:(?:\[deleted\])?\s*)?Based on the context, the disorder may be:"
        match = re.search(text_patron, text, re.DOTALL)  # <-- Add re.DOTALL to get line breaks
        if match:
            # Extract and clean the statement text
            statement = match.group(1).strip()
            response = entry['response'].strip()
            return {'statement': statement, 'response': response}
        # If no match, record an error and skip this entry
        #cont_error += 1
        return None
    
    ## Load the dataset and split it into train and test sets
    # Load the dataset from HuggingFace
    ds_1 = load_dataset("sajjadhadi/Mental-Disorder-Detection-Data")
    # Get all data available, whether it is from the test and train sets
    train_statements = [extract_hugging_1(e) for e in ds_1['train']]
    test_statements = [extract_hugging_1(e) for e in ds_1['test']]
    conv_hugg_1 = train_statements + test_statements


    ## Check for unique responses/labels in the dataset
    # Eliminate None entries
    valid_entries = [e for e in conv_hugg_1 if e is not None]
    # Extract responses
    responses = [e["response"] for e in valid_entries]
    # Eliminate duplicate responses
    unique_responses = set(responses)
    print(f"Found {len(unique_responses)} unique labels/responses in Hugging_1 dataset:")
    for r in unique_responses:
        print("-", r)

    # Clean entries
    for entry in conv_hugg_1:
        label = entry.get("response", "")                    # Get original label (e.g., "Anxiety")
        mapped_label = label_mapping.get(label, "")          # Map it to the new format -> label_mapping dictionary
        if mapped_label in LABELS:                           # Check if it's a mapped label
            if remove_original_labels:
                entry["response"] = ""                       # Remove the original label
            else:
                entry["response"] = mapped_label             # Replace with the mapped label
        else:
            entry["response"] = "" 


    
    process_dicts_to_json(conv_hugg_1, SPLIT_PATTERN_1, text_key="statement", label_key="response", output_filename="hugg_1.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_2():
    """https://huggingface.co/datasets/marmikpandya/mental-health"""
    ds_2 = load_dataset("marmikpandya/mental-health")
    conv_hugg_2 = ds_2['train']['input']
    process_texts_to_json(conv_hugg_2, SPLIT_PATTERN_1, output_filename="hugg_2.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_3():
    """https://huggingface.co/datasets/fadodr/mental_health_dataset"""
    ds_3 = load_dataset("fadodr/mental_health_dataset")
    # Combine train and test sets
    conv_1 = list(ds_3['train']['client'])
    conv_2 = list(ds_3['test']['client'])
    conv_hugg_3 = conv_1 + conv_2
    process_texts_to_json(conv_hugg_3, SPLIT_PATTERN_1, output_filename="hugg_3.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_4():
    """https://huggingface.co/datasets/fadodr/mental_health_therapy"""
    ds_4 = load_dataset("fadodr/mental_health_therapy")
    conv_1 = list(ds_4['train']['input'])
    conv_2 = list(ds_4['test']['input'])
    conv_hugg_4 = conv_1 + conv_2
    process_texts_to_json(conv_hugg_4, SPLIT_PATTERN_1, output_filename="hugg_4.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_5():
    """https://huggingface.co/datasets/psycode1/psyset"""
    def extract_hugg_5(text):
        """
        Extracts the content between the '<s>[INST]' tag and the sequence '", nan' in a string. Specific for this dataset.

        Args:
        text (str): The raw text containing an instruction tag and trailing ', nan'.

        Returns:
        str or None: The trimmed content inside the INST tag, or None if no match is found.
        """
        # Define regex pattern:
        # - '<s>\[INST\]' matches the literal start tag '<s>[INST]'
        # - '(.*?)' lazily captures any characters up to the first occurrence of the ending delimiter
        # - '", nan' marks the end boundary (double quote, comma, space, 'nan')
        patron = r"<s>\[INST\](.*?)\", nan"

        # Use DOTALL so '.' matches newline characters as well
        match = re.search(patron, text, re.DOTALL)

        if match:
            # Return the captured group, stripped of leading/trailing whitespace
            return match.group(1).strip()

        # If no pattern match, return None
        return None
    
    ds_5 = load_dataset("psycode1/psyset")
    inputs_raw = ds_5['train']['text']
    conv_hugg_5 = [extract_hugg_5(t) for t in inputs_raw]
    process_texts_to_json(conv_hugg_5, SPLIT_PATTERN_1, output_filename="hugg_5.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_6():
    """https://huggingface.co/datasets/marmikpandya/mental-health"""
    ds_6 = load_dataset("marmikpandya/mental-health")
    conv_hugg_6 = ds_6['train']['input']
    process_texts_to_json(conv_hugg_6, SPLIT_PATTERN_1, output_filename="hugg_6.json", max_interventions=MAX_INTERVENTIONS)

def load_hugging_7():
    """https://huggingface.co/datasets/Amod/mental_health_counseling_conversations"""
    ds_7 = load_dataset("Amod/mental_health_counseling_conversations")
    hugg_7 = ds_7['train']['Context']
    process_texts_to_json(hugg_7, SPLIT_PATTERN_1, output_filename="hugg_7.json", max_interventions=MAX_INTERVENTIONS)



def load_hugging_8():
    """https://huggingface.co/datasets/cypsiSAS/transformed_Suicidal_ideation"""
    def extract_hugg_8(text):
        """
        Extracts the content between the closing [/INST] tag and the </s> tag. Specific for this dataset.

        Args:
            text (str): A string containing something like:
                <s>[INST] … [/INST] text-to-extract </s>

        Returns:
            str | None: The trimmed text found between [/INST] and </s>,
                        or None if the pattern isn’t present.
        """
        # Define regex pattern:
        patron = r"\[/INST\]\s*(.*?)\s*</s>"

        # Use DOTALL so '.' matches newline characters as well
        match = re.search(patron, text, re.DOTALL)

        if match:
            # Return the captured group, stripped of leading/trailing whitespace
            return match.group(1).strip()

        # If no pattern match, return None
        return None
    
    ds_8 = load_dataset("cypsiSAS/transformed_Suicidal_ideation")
    inputs_raw = ds_8['train']['formatted']
    conv_hugg_8 = [extract_hugg_8(t) for t in inputs_raw]

    process_texts_to_json(conv_hugg_8, SPLIT_PATTERN_1, output_filename="hugg_8.json", max_interventions=MAX_INTERVENTIONS)

def load_hugging_9():
    """https://huggingface.co/datasets/fanyin3639/test_test_self_harm_all_levels"""
    ds_9 = load_dataset("fanyin3639/test_test_self_harm_all_levels")
    hugg_9 = ds_9['train']['prompt']
    hugg_9 = [
        {"input": p, "label": "self-harm"}
        for p in hugg_9
    ]
    process_dicts_to_json(hugg_9, SPLIT_PATTERN_1, text_key='input', label_key='label', output_filename="hugg_9.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_10():
    """https://huggingface.co/datasets/arianaazarbal/self-harm-synthetic-eval"""
    # Mapping of label variants that are studied
    label_mapping = {
        "hurting_oneself": "self-harm",
        "suicidal_ideation": "suicidal_ideation"
    }

    ds_10 = load_dataset("arianaazarbal/self-harm-synthetic-eval")
    # Extract texts and labels from train and eval splits
    train_texts = ds_10['train']['instruction']
    train_labels = ds_10['train']['category']

    # Combine into a list of dicts so row-level filtering is straightforward
    data = [
        {'text': t, 'label': l}
        for t, l in zip(train_texts, train_labels)
    ]

    # Label distribution
    all_labels = [entry['label'] for entry in data]
    unique_labels = set(all_labels)
    print(unique_labels)

    # Filter data to keep only entries with labels in mapping, and replace them
    cleaned_data = []
    for entry in data:
        original = entry['label']
        if original in label_mapping:
            entry['label'] = label_mapping[original]
            cleaned_data.append(entry)

    process_dicts_to_json(cleaned_data, SPLIT_PATTERN_1, text_key="text", label_key="label", output_filename="hugg_10.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_11():
    """https://huggingface.co/datasets/richie-ghost/suicidal_finetune"""
    label_mapping = {
        "Consumption": "substance_abuse_or_withdrawal",
        "Suicidal planning": "suicidal_ideation"
    }

    ds_11 = load_dataset("richie-ghost/suicidal_finetune")
    # Extract texts and labels from train and eval splits
    train_texts = list(ds_11['train']['Text'])
    train_labels = list(ds_11['train']['Label'])
    eval_texts  = list(ds_11['eval']['Text'])
    eval_labels  = list(ds_11['eval']['Label'])

    # Combine into a list of dicts so row-level filtering is straightforward
    data = [
        {'text': t, 'label': l}
        for t, l in zip(train_texts + eval_texts, train_labels + eval_labels)
    ]
    # Label distribution
    all_labels = [entry['label'] for entry in data]
    unique_labels = set(all_labels)
    print(unique_labels)

    # Filter data to keep only entries with labels in mapping, and replace them
    cleaned_data = []
    for entry in data:
        original = entry['label']
        if original in label_mapping:
            entry['label'] = label_mapping[original]
            cleaned_data.append(entry)

    process_dicts_to_json(cleaned_data, SPLIT_PATTERN_1, text_key="text", label_key="label", output_filename="hugg_11.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_16K():
    """ https://huggingface.co/datasets/ShenLab/MentalChat16K"""
    ds_16K = load_dataset("ShenLab/MentalChat16K")
    conv_hugg_16K = ds_16K['train']['input']
    # Special sentence splitting pattern: A special rule to break on a double-quote followed by optional whitespace and a newline ("\s*\n), treating that sequence itself as the split point.
    split_pattern_16k = r'(?:"\s*\n)|(?<=(?:\.{3}|\?\?|!!|\?\!|!\?|[.?!]))|\n'
    process_texts_to_json(conv_hugg_16K, split_pattern_16k, output_filename="hugg_16K.json", max_interventions=MAX_INTERVENTIONS)


def load_hugging_100K_synthetic():
    """https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic"""
    ds_100K = load_dataset("jerryjalapeno/nart-100k-synthetic")
    conversations = ds_100K['train']['conversations']

    # Extract only where "from" is "human"
    # Iterates over each conversation in ds_100K['train']['conversations'], extracts and trims all human messages (msg["from"] == "human" with a nonempty value),
    # then joins them with spaces, producing a list where each entry is the concatenated human dialogue from one conversation.
    hugging_100K = [
        " ".join([msg["value"].strip() for msg in convo if msg.get("from") == "human" and msg.get("value")])
        for convo in ds_100K['train']['conversations']
    ]


    process_texts_to_json(hugging_100K, SPLIT_PATTERN_1, output_filename="hugg_100K.json", max_interventions=MAX_INTERVENTIONS)


def load_and_save_dataset(dataset):
    #check if str is digit
    dataset = dataset.lower()
    if dataset == "hugg_1":
        load_hugging_1()
    elif dataset == "hugg_2":
        load_hugging_2()
    elif dataset == "hugg_3":
        load_hugging_3()
    elif dataset == "hugg_4":
        load_hugging_4()
    elif dataset == "hugg_5":
        load_hugging_5()
    elif dataset == "hugg_6":
        load_hugging_6()
    elif dataset == "hugg_7":
        load_hugging_7()
    elif dataset == "hugg_8":
        load_hugging_8()
    elif dataset == "hugg_9":
        load_hugging_9()
    elif dataset == "hugg_10":
        load_hugging_10()
    elif dataset == "hugg_11":
        load_hugging_11()
    elif dataset == "hugg_16k":
        load_hugging_16K()
    elif dataset == "hugg_100k":
        load_hugging_100K_synthetic()
    else:
        raise ValueError(f"Dataset {dataset} not recognized. Please check the dataset name.")
    print(f"\tDataset {dataset} loaded successfully.")