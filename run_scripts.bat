::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Label validation dataset with three different models
:: python scripts/llm_as_judge.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts/llm_as_judge.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts/llm_as_judge.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Evaluate agreement between human and LLM labels (anonymized humans)
:: python scripts\agreement_rate.py ^
::   --human_paths H1_labeled_n206_s42.json ^
::                 H2_labeled_n206_s42.json ^
::                 H3_labeled_n206_s42.json ^
::                 H4_labelled_n206_s42.json ^
::   --llm_paths gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json ^
::              gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json ^
::              gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json ^
::              gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json ^
::              gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json ^
::              gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json ^
::              meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json ^
::              meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json ^
::              meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json ^
::   --original_path data\processed\sampled_dataset_n_200_merged_n50-noSeed_156-s42.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Label dataset with n=2000 samples with gpt-4o-mini (model with more agreement)
:: python scripts/llm_as_judge.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get label consensus between the different iterations for n=200 using the best model - break draws between humans
::python scripts\merge_labeled_datasets.py ^
::--input-files   data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json ^
::                data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json ^
::                data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json ^
::--output-file  gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-merged_labels.json

:: Get label consensus between humans - break draws using label consensus of gpt 4o mini
:: python scripts\merge_labeled_datasets.py ^
:: --input-files   data\human_label\H1_labeled_n206_s42.json ^
::                data\human_label\H2_labeled_n206_s42.json ^
::                data\human_label\H3_labeled_n206_s42.json ^
::                data\human_label\H4_labelled_n206_s42.json ^
::                data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-merged_labels.json ^
:: --output-file human-labeled-sampled_dataset_n206_s42-merged_labels.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get agreement rate between the different iterations for n=2000
:: python scripts\agreement_rate.py ^
:: --llm_paths     gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122539.json ^
::                 gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122928.json ^
::                 gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122930.json ^
:: --original_path data\processed\sampled_dataset_n_2046_nPerD168_seed0.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get merged label consensus between the different iterations for n=2000
:: python scripts\merge_labeled_datasets.py ^
:: --input-files   data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122539.json ^
::                data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122928.json ^
::                data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-20250825-122930.json ^
:: --output-file gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Appropriateness agreement (anonymized humans)
:: python scripts\appropriateness_agreement.py ^
::   --sampled_path data\llm_evaluator\sampled\sampled_lowest_scores_n200.json ^
::   --llm_evaluator_dirs gpt-5-nano=data\llm_evaluator\gpt-5-nano\n_200\merged ^
::                       meta-llama=data\llm_evaluator\meta-llama\n_200\merged ^
::   --human_score_paths data\human_label\H1_scores_n206_s42.json ^
::                      data\human_label\H2_scores_n206_s42.json ^
::   --output_dir outputs\appropriateness_agreement ^
::   --min_rating 1 ^
::   --max_rating 5
::
:: python scripts\appropriateness_agreement_enhanced.py ^
::   --sampled_path data\llm_evaluator\sampled\sampled_lowest_scores_n200.json ^
::   --llm_evaluator_dirs gpt-5-nano=data\llm_evaluator\gpt-5-nano\n_200\merged ^
::                       meta-llama=data\llm_evaluator\meta-llama\n_200\merged ^
::   --human_score_paths data\human_label\H1_scores_n206_s42.json ^
::                      data\human_label\H2_scores_n206_s42.json ^
::   --output_dir outputs\appropriateness_agreement_enhanced ^
::   --min_rating 1 ^
::   --max_rating 5 ^
::   --aggregation_method mean

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get Answers to conversations - n= 200
:: python scripts\get_answer_to_conversations.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts\get_answer_to_conversations.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json --temp-path data\llm_answer\TEMP_gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-171912.json
:: python scripts\get_answer_to_conversations.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts\get_answer_to_conversations.py --model deepseek-chat --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts\get_answer_to_conversations.py --model grok-4-fast-non-reasoning --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get Answers to conversations - n= 2000 - x3 runs per model
:: python scripts\get_answer_to_conversations.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model deepseek-chat --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model grok-4-fast-non-reasoning --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get Evaluations for n=200. Labels the human agreement (we have it). 3 per each model answer iteration (9 per model answering)
:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data/llm_answer/gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-170248.json ^
::    --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data/llm_answer/gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-182618.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data/llm_answer/gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-184722.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-171912.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-174234.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-180602.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132221.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132715.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132718.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20251105-120703.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-155050.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-163353.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20251106-162906.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-155014.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::     --model gpt-4o-mini ^
::     --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-163306.json ^
::     --label-path data\human_label\human-labeled-sampled_dataset_n206_s42-merged_labels.json

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get Evaluations for n=2000. 3 per each model answer iteration (9 per model answering)
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-163348.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-202644.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-234120.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-160821.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-230939.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-053015.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: python scripts\llm_as_protocol_evaluator.py --model gpt-4o-mini  --answered-path data/llm_answer\meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728.json  --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json


:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-121458.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json

:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153711.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json

:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153713.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json

:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164208.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164210.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json
:: 
:: 
:: python scripts\llm_as_protocol_evaluator.py ^
::    --model gpt-4o-mini ^
::    --answered-path data\llm_answer\grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164211.json ^
::    --label-path data\llm_label\gpt-4o-mini-labeled-sampled_dataset_n_2046_nPerD168_seed0-merged-labels.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Merge evaluations for n=2000.
:: python scripts\merge_evaluations.py --folder data/llm_evaluator/n_2000
:: python scripts\merge_evaluations.py --folder data/llm_evaluator/n_200


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: Sample n=200 answers based on evaluation scores
:: # Sample with HIGHEST scores (best answers)
:: python sample_answer_per_score.py --criteria highest --output_name sampled_best_answers_n200
:: 
:: # Sample with LOWEST scores (worst answers)
:: python sample_answer_per_score.py --criteria lowest --output_name sampled_lowest_scores_n200
:: 
:: # Sample with MEDIAN scores (middle ground)
:: python sample_answer_per_score.py --criteria median --output_name sampled_median_scores_n200
:: 
:: # Sample with RANDOM selection (unbiased)
:: python sample_answer_per_score.py --criteria random --output_name sampled_random_scores_n200
:: 
:: # Compare distributions across all 4 strategies
:: python compare_sampling_strategies.py
:: # Check which entries have all null evaluations
:: python debug_nulls.py
:: 
:: # Verify the sampled dataset
:: python verify_fix.py
:: 
:: # Check dataset structure
:: python verify_sampled.py


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


::::::::::::::::::::::::::::::::::::::::::::::::::
:: Compute statistics n=200
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
::  data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-170248_merged.json ^
::  data/llm_evaluator/n_200/merged/gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-182618_merged.json ^
::  data/llm_evaluator/n_200/merged/gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-184722_merged.json
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^ 
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-171912_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-174234_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-180602_merged.json
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^ 
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132221_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132715_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250822-132718_merged.json


:: python scripts\compute_statistics_about_evaluation.py --input-files ^ 
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20251105-120703_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-155050_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-163353_merged.json
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^ 
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20251106-162906_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-155014_merged.json ^
:: data\llm_evaluator\n_200\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20260121-163306_merged.json



:: :: Compute statistics n=2000
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-163348_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-202644_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-234120_merged.json 
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-160821_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-230939_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-053015_merged.json 
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728_merged.json
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-121458_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153711_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153713_merged.json
:: 
:: python scripts\compute_statistics_about_evaluation.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164208_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164210_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164211_merged.json



:: Compute statistics n=2000 and visualizations
:: python scripts\create_stat_vizs.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-163348_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-202644_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-234120_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-160821_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-230939_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-053015_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-121458_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153711_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153713_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164208_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164210_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164211_merged.json


:: python utils\split_low_eval_by_label.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-163348_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-202644_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-234120_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-160821_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-230939_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-053015_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-121458_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153711_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_deepseek-chat-answers-sampled_dataset_n_2046_nPerD168_seed0-20251105-153713_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164208_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164210_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_grok-4-fast-non-reasoning-answers-sampled_dataset_n_2046_nPerD168_seed0-20251106-164211_merged.json ^
:: --threshold 2