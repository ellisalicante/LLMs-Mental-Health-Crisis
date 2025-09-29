Here we have the following datasets in json


1. **`merged_dataset_all.json`**: Not Included due to file size (340MB). This file contains the merged (non-labelled) dataset from all individual datasets. **Created by `scripts/load_merge_dataset.py`**.
* Number of datasets processed: 13
* Total number of conversations: 264,966
   * With labels (from original datasets): 1,250 (0.4%)
* Total number of interventions: 3,714,713
  
2. **`sampled_dataset_n{sampled}_seed{seed}.json`** is a light-weight example of what the merged (non-labelled) dataset looks like. **Created by `scripts/sample_dataset.py`**.
* `n` is the sampled conversations from each individual dataset. Configured as `DEFAULT_N` in `src/config.py` or parameter in `scripts/sample_dataset.py`.
* `seed` is the random seed used to sample the conversations. Configured as `DEFAULT_SEED` in `src/config.py` or parameter in `scripts/sample_dataset.py`.
* Includes:
  * `sampled_dataset_n_200_merged_n50-noSeed_156-s42.json`: Validation set. N=200. Includes 200 conversations sampled from the merged dataset, which are manually labeled in `data/human_label/` and labeled by llms in `data/llm_label/`. 
  * `sampled_dataset_n_2046_nPerD168_seed0`: Labeled dataset by `4o-mini`. N=2000. Includes 2000 conversations sampled from the merged dataset, which are Labeled dataset by `4o-mini` in `data/llm_label/`.