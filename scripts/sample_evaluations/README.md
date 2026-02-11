# Sample Evaluations Scripts

This folder contains scripts for sampling conversations based on evaluation results.

## Main Scripts

### `sample_answer_per_score.py`
**Purpose**: Main script to sample answers based on gpt-4o-mini evaluation scores.

**Usage**:
```bash
cd scripts/sample_evaluations
python sample_answer_per_score.py --criteria highest --output_name my_sampled_dataset
```

**Arguments**:
- `--input_dir`: Directory with merged evaluation files (default: `../../data/llm_evaluator/gpt-4o-mini/n_200/merged`)
- `--output_dir`: Output directory for sampled dataset (default: `../../data/llm_evaluator/sampled`)
- `--output_name`: Name of output file without extension
- `--criteria`: Sampling strategy - `highest`, `lowest`, `median`, or `random` (default: `highest`)

**What it does**:
- Loads 15 evaluation files (3 iterations × 5 models)
- For each user input (206 total), selects one answer based on the chosen criteria
- Handles cases where all 15 evaluations are null (16 entries)
- Saves sampled dataset with source tracking metadata

### `compare_sampling_strategies.py`
**Purpose**: Compare score distributions across different sampling strategies.

**Usage**:
```bash
python compare_sampling_strategies.py
```

**What it does**:
- Loads sampled datasets from all 4 strategies (highest, lowest, median, random)
- Displays detailed score distributions with visual bars
- Shows summary statistics table
- Shows score range distribution table (1-2, 2-3, 3-4, 4-5)

**Output**:
- Detailed statistics for each strategy
- Visual distribution charts
- Comparison tables

## Utility Scripts

### `debug_nulls.py`
**Purpose**: Identify entries where all evaluations are null.

**Usage**:
```bash
python debug_nulls.py
```

**What it does**:
- Checks all 15 evaluation files
- Reports entries where ALL evaluations are null
- Reports entries where SOME evaluations are null

### `verify_fix.py`
**Purpose**: Verify that null handling in sampled dataset is correct.

**Usage**:
```bash
python verify_fix.py
```

**What it does**:
- Loads the sampled dataset (v2)
- Counts null vs non-null evaluations
- Verifies null count matches expected value (16)

### `verify_sampled.py`
**Purpose**: Verify the structure and uniqueness of sampled dataset.

**Usage**:
```bash
python verify_sampled.py
```

**What it does**:
- Checks for duplicate dataset_ids
- Shows score distribution
- Validates dataset structure

## Data Flow

```
Input: data/llm_evaluator/gpt-4o-mini/n_200/merged/*.json (15 files)
         ↓
   sample_answer_per_score.py (with criteria)
         ↓
Output: data/llm_evaluator/sampled/sampled_*.json
         ↓
   compare_sampling_strategies.py
         ↓
   Analysis tables and distributions
```

## Key Statistics

- **Total user inputs**: 206
- **Evaluation files**: 15 (3 iterations × 5 models)
- **Null evaluations**: 16 entries (where humans didn't agree on labels)
- **Models**: deepseek-chat, gpt-4o-mini, gpt-5-nano, grok-4-fast-non-reasoning, meta-llama-Llama-4-Scout-17B-16E-Instruct

## Sampling Strategy Results

| Strategy | Mean Score | % in 4.0-5.0 range | Best Use Case |
|----------|------------|-------------------|---------------|
| **Highest** | 4.99 | 99.5% | Highest quality answers |
| **Median** | 4.76 | 95.8% | Balanced selection |
| **Random** | 4.69 | 94.2% | Unbiased across models |
| **Lowest** | 3.99 | 72.6% | Testing/analysis of weaknesses |
