import os
from dotenv import load_dotenv
load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
GROQ_API_KEY = os.getenv("GROK_API_KEY")

LABELS = {
    "suicidal_ideation",
    "self-harm",
    "violent_thoughts",
    "substance_abuse_or_withdrawal",
    "anxiety_crisis", # includes panic attack
    "risk_taking_behaviours",
    "no_crisis"
}

AVAILABLE_DATASETS = ['hugg_1', 'hugg_2', 'hugg_3', 'hugg_4', 'hugg_5',
            'hugg_6', 'hugg_7', 'hugg_8', 'hugg_9', 'hugg_10', 'hugg_11',
            'hugg_16k', 'hugg_100k']

# Seed for reproducibility
DEFAULT_SEED = 42

# This pattern splits text either right after any sentence-ending mark: an ellipsis (…), double or mixed punctuation like ??, !!, ?!, !?, or any single . ? or !, or at every newline. By using a positive lookbehind (?<=…) for those punctuation sequences, the split keeps the delimiters attached to the preceding segment, while |\n treats line breaks as separate split points.
SPLIT_PATTERN_1 = r'(?<=(?:\.{3}|\?\?|!!|\?\!|!\?|[.?!]))|\n'

# max allowed number of interventions per conversation
MAX_INTERVENTIONS = 40


# retrieving specific number of conversations for concrete datasets WHEN MERGING
CUSTOM_SAMPLE_SIZES = {
 # "hugg_1": 10,
 # "hugg_5": 50,
}
# Set default number of conversations to get per dataset WHEN MERGING
DEFAULT_N = 5 

AVAILABLE_LLMS = {"gpt-4o-mini", "gpt-5-nano", "meta-llama/Llama-4-Scout-17B-16E-Instruct"} #gpt-3.5-turbo, llama-3.3-70b-versatile, 

IND_DATASETS_DIR = "data/raw"
MERGED_DATASET_DIR = "data/processed"
SAMPLED_DATASET_DIR = "data/processed"
LLM_LABEL_DIR = "data/llm_label"
HUMAN_LABEL_DIR = "data/human_label"
LLM_ANSWER_DIR = "data/llm_answer"
LLM_EVALUATOR_DIR = "data/llm_evaluator"

PROTOCOL_DIR = os.path.join(LLM_EVALUATOR_DIR, "protocol.csv")