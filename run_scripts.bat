::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Label validation dataset with three different models
:: python scripts/llm_as_judge.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts/llm_as_judge.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts/llm_as_judge.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Evaluate agreement between human and LLM labels
:: python scripts\agreement_rate.py ^
::   --human_paths EPV_labeled_n206_s42.json ^
::                 JLA_labeled_n206_s42.json ^
::                 MB_labeled_n206_s42.json ^
::                 MI_labelled_n206_s42.json ^
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
:: --input-files   data\human_label\EPV_labeled_n206_s42.json ^
::                data\human_label\JLA_labeled_n206_s42.json ^
::                data\human_label\MB_labeled_n206_s42.json ^
::                data\human_label\MI_labelled_n206_s42.json ^
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
:: Get Answers to conversations - n= 200
:: python scripts\get_answer_to_conversations.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json
:: python scripts\get_answer_to_conversations.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json --temp-path data\llm_answer\TEMP_gpt-5-nano-answers-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-171912.json
:: python scripts\get_answer_to_conversations.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_200_merged_n50-noSeed_156-s42.json


:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Get Answers to conversations - n= 2000
:: python scripts\get_answer_to_conversations.py --model gpt-4o-mini --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model gpt-5-nano --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json
:: python scripts\get_answer_to_conversations.py --model meta-llama/Llama-4-Scout-17B-16E-Instruct --dataset-path data/processed/sampled_dataset_n_2046_nPerD168_seed0.json


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



:::::::::::::::::::::::::::::::::::::::::::::::::::
:: Merge evaluations for n=2000.
:: python scripts\merge_evaluations.py --folder data/llm_evaluator/n_2000
:: python scripts\merge_evaluations.py --folder data/llm_evaluator/n_200


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
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723_merged.json data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725_merged.json data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728_merged.json
:: 

:: :: Compute statistics n=2000 and visualizations
:: python scripts\create_stat_vizs.py --input-files ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-163348_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-202644_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-4o-mini-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-234120_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-160821_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250821-230939_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_gpt-5-nano-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-053015_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132723_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132725_merged.json ^
:: data\llm_evaluator\n_2000\merged\gpt-4o-mini-evaluation_meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled_dataset_n_2046_nPerD168_seed0-20250822-132728_merged.json



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
:: ---threshold 2