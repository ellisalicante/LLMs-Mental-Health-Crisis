"""The content of the HuggingFace datasets can be in dictionary or list of strings format. Therefore, two functions are defined that generate the same output structure but for the two different inputs."""

import regex as re
import json
from collections import Counter
import os

from src.config import IND_DATASETS_DIR


def clean_sentence(s):
    '''
    It filters out a possible not meaningful or unvalid string and returns the already cleaned string.
    '''

    # Drop sentence completely if…

    # Too short (< 2 chars)
    if len(s) < 2:
        return ""

    # Only quotes or ellipsis
    if s in ['"', "'", '""', "'''", "..."]:
        return ""

    # Only points (with or without space)
    if re.fullmatch(r"\.*", s) or re.fullmatch(r"(\.\s*)+", s):
        return ""

    # Only numbers
    if re.fullmatch(r"\d+", s):
        return ""

    # URLs or media extensions
    if re.search(r"http\S+|www\.\S+|\b(?:reddit\.com|puu\.sh|mp4|jpg|png|gif)\b", s):
        return ""

    # Just punctuation/symbols, e.g. "!!!" or "..."
    if re.fullmatch(r"[^\w\s]+", s):
        return ""

    # Otherwise, remove unwanted parts but keep the rest:

    # Text inside square brackets (and the brackets)
    s = re.sub(r"\[.*?\]", "", s)

    # All backslashes
    s = s.replace("\\", "")

    # Strip again
    s = s.strip()

    # Return the cleaned string (or “” if it became empty)
    return s


def process_texts_to_json(all_conversations, split_pattern, output_filename, max_interventions=40):
    """
    Processes a list of conversation strings into JSON entries format.

    Parameters:
      all_conversations: List of text strings
      split_pattern: regex pattern to split conversations into interventions
      output_filename: path for writing resulting JSON file
      max_interventions: max allowed number of interventions per conversation

    Behavior:
      - Removes None entries
      - Removes duplicate conversations
      - Splits each conversation by the given pattern
      - Cleans and strips each intervention
      - Discards conversations with zero or too many interventions ( > max_interventions)
      - Assigns an empty string to the "label" field for all entries
      - Reports summary statistics and writes filtered data to JSON
    """

    original_len = len(all_conversations)

    # Remove None entries
    all_conversations = [conversation for conversation in all_conversations if conversation is not None]

    # Remove duplicates maintaining the order
    seen = set()
    unique_conversations = []
    for conversation in all_conversations:
        if conversation not in seen:
            seen.add(conversation)
            unique_conversations.append(conversation)
    all_conversations = unique_conversations

    # Check duplicates removed
    num_duplicates = original_len - len(all_conversations)

    final_data = []
    conversation_counts = []

    for conversation in all_conversations:
        interventions = []
        # Split the conversation into different interventions
        for intervention in re.split(split_pattern, conversation):
            # Remove spaces and line breaks from the intervention
            cleaned_intervention = clean_sentence(intervention.strip())
            if cleaned_intervention:
                interventions.append(cleaned_intervention)

        # Only keep conversation if it has less than max_interventions
        if 0 < len(interventions) <= max_interventions:
            final_data.append({
                "inputs": interventions,
                "label": ""
            })
            conversation_counts.append(len(interventions))

    # Interventions count distribution
    num_interventions_distribution = Counter(conversation_counts)

    # Output summary
    print(f"Original number of full conversations: {original_len}")
    print(f"Duplicates removed: {num_duplicates}")
    print(f"Remaining conversations after filtering (≤ {max_interventions} sentences): {len(final_data)}")

    print("Num interventions count distribution:")
    for num_interventions, count in sorted(num_interventions_distribution.items()):
        print(f"{num_interventions} interventions: {count} conversations")

    if final_data:
        print("\nExample entry:")
        print(final_data[0])

    # Save to JSON
    with open(os.path.join(IND_DATASETS_DIR,output_filename), "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)



def process_dicts_to_json(dict_all_conversations, split_pattern, text_key, label_key, output_filename, max_interventions=40):
    """
    Processes a list of conversation dicts into JSON entries.

    Parameters:
      dict_all_conversations: Raw conversation entries where each dict contains at least a text field and optionally a label
      split_pattern: regex pattern to split conversations into interventions
      text_key: Key in each dict where the conversation text is located
      label_key: Key in each dict where the existing label (if any) is located; missing labels default to empty string.
      output_filename: path for writing resulting JSON file
      max_interventions: max allowed number of interventions per conversation

    Behavior:
      - Removes None or entries missing the text_key
      - Eliminates duplicates based on (text, label) pairs
      - Splits text into clean interventions.
      - Filters out conversations with zero or too many interventions ( > max_interventions)
      - Assigns an empty string to "label" for each output entry.
      - Prints summary statistics and writes out filtered data to JSON.
    """
    original_len = len(dict_all_conversations)

    # Remove none entries and items missing the text_key
    dict_all_conversations = [conv for conv in dict_all_conversations if conv is not None and text_key in conv]

    # Remove duplicates based on the combination (text, label)
    seen = set()        # hold tuples of (text, label)
    conversations = []
    for conv in dict_all_conversations:
        text_val = conv[text_key]
        # If there’s a label_key use it, otherwise treat label as empty string
        label_val = conv[label_key] if label_key in conv else ""
        pair = (text_val, label_val)
        # Only add the first time we see each (text, label)
        if pair not in seen:
            seen.add(pair)
            conversations.append(conv)

    # Check duplicates removals
    num_duplicates = original_len - len(conversations)

    # Now split each remaining text into “clean” interventions
    final_data = []
    conversation_counts = []

    for conv in conversations:
        conversation = conv[text_key]

        # Split text into interventions and eliminate whitespace
        interventions = []
        for intervention in re.split(split_pattern, conversation):
            cleaned_intervention = intervention.strip()
            if cleaned_intervention:
                interventions.append(cleaned_intervention)

        # Only keep conversation if it has less than max_interventions
        if 0 < len(interventions) <= max_interventions:
            # If there’s a label_key use it, otherwise treat label as empty string
            label_val = conv.get(label_key, "")
            final_data.append({
                "inputs": interventions,
                "label": label_val
            })
            conversation_counts.append(len(interventions))

    num_interventions_distribution = Counter(conversation_counts)

    # Output summary
    print(f"Original number of full conversations: {original_len}")
    print(f"Duplicates removed: {num_duplicates}")
    print(f"Remaining conversations after filtering (≤ {max_interventions} sentences): {len(final_data)}")

    print("Num interventions count distribution:")
    for num_interventions, count in sorted(num_interventions_distribution.items()):
        print(f"{num_interventions} interventions: {count} conversations")

    if final_data:
        print("\nExample entry:")
        print(final_data[0])

    # Save to JSON
    with open(os.path.join(IND_DATASETS_DIR,output_filename), "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)