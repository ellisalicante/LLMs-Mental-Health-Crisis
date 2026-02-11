# Agreement Rate Report
## Dataset Summary
- Total number of conversations: 206
- Human annotators: 4
    * H1_labeled_n206_s42.json: 206 annotations
    * H2_labeled_n206_s42.json: 206 annotations
    * H3_labeled_n206_s42.json: 206 annotations
    * H4_labelled_n206_s42.json: 206 annotations
- LLM annotators: 9
    * gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json: 206 annotations
    * gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json: 206 annotations
    * gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json: 206 annotations
    * gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json: 206 annotations
    * gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json: 206 annotations
    * gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json: 206 annotations
    * meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json: 206 annotations
    * meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json: 206 annotations
    * meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json: 206 annotations
## Pairwise Agreement Rates
### `H1_labeled_n206_s42.json` and `H2_labeled_n206_s42.json`:
	* 🟩 Agreement Rate: 67.48%
	* 🧠 Cohen's Kappa: 0.58
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `H2_labeled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               21 |          34 |                        1 |           0 |                               1 |                   1 |                  1 |  0 |
| no_crisis                     |                0 |          61 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           8 |                        0 |           2 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           5 |                        0 |          13 |                               1 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        4 |           0 |                              11 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           0 |                               0 |                  29 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   2 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.576271 |                0.0169492 |    0        |                       0.0169492 |           0.0169492 |          0.0169492 |  0 |
| no_crisis                     |        0.576271  |    0        |                0.727273  |    0.25     |                       0.0625    |           0.121212  |          0         |  0 |
| risk_taking_behaviours        |        0.0169492 |    0.727273 |                0         |    0.181818 |                       0.25      |           0.0909091 |          0         |  0 |
| self-harm                     |        0         |    0.25     |                0.181818  |    0        |                       0.05      |           0.05      |          0         |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |    0.0625   |                0.25      |    0.05     |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0169492 |    0.121212 |                0.0909091 |    0.05     |                       0         |           0         |          0.333333  |  0 |
| violent_thoughts              |        0.0169492 |    0        |                0         |    0        |                       0         |           0.333333  |          0         |  0 |
|                               |        0         |    0        |                0         |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.576 | 59 |
| no_crisis | n/a | n/a | 61 |
| risk_taking_behaviours | no_crisis | 0.727 | 11 |
| self-harm | no_crisis | 0.250 | 20 |
| substance_abuse_or_withdrawal | risk_taking_behaviours | 0.250 | 16 |
| suicidal_ideation | no_crisis | 0.121 | 33 |
| violent_thoughts | suicidal_ideation | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.727 | 0.000 | 0.727 |
| anxiety_crisis | no_crisis | 0.576 | 0.576 | 0.000 |
| suicidal_ideation | violent_thoughts | 0.333 | 0.000 | 0.333 |
| no_crisis | self-harm | 0.250 | 0.000 | 0.250 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.250 | 0.000 | 0.250 |

### `H1_labeled_n206_s42.json` and `H3_labeled_n206_s42.json`:
	* 🟩 Agreement Rate: 67.48%
	* 🧠 Cohen's Kappa: 0.59
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `H3_labeled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               34 |          18 |                        2 |           0 |                               2 |                   3 |                  0 |  0 |
| no_crisis                     |                6 |          39 |                        7 |           2 |                               2 |                   4 |                  1 |  0 |
| risk_taking_behaviours        |                1 |           3 |                        4 |           0 |                               0 |                   2 |                  1 |  0 |
| self-harm                     |                1 |           1 |                        1 |          16 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                3 |           1 |                        2 |           0 |                               0 |                  27 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   2 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.403445  |                0.124807  |   0.05      |                       0.0338983 |           0.141757  |          0         |  0 |
| no_crisis                     |        0.403445  |   0         |                0.387481  |   0.0827869 |                       0.0952869 |           0.0958768 |          0.0163934 |  0 |
| risk_taking_behaviours        |        0.124807  |   0.387481  |                0         |   0.05      |                       0         |           0.242424  |          0.0909091 |  0 |
| self-harm                     |        0.05      |   0.0827869 |                0.05      |   0         |                       0         |           0.05      |          0         |  0 |
| substance_abuse_or_withdrawal |        0.0338983 |   0.0952869 |                0         |   0         |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.141757  |   0.0958768 |                0.242424  |   0.05      |                       0         |           0         |          0.333333  |  0 |
| violent_thoughts              |        0         |   0.0163934 |                0.0909091 |   0         |                       0         |           0.333333  |          0         |  0 |
|                               |        0         |   0         |                0         |   0         |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.305 | 59 |
| no_crisis | risk_taking_behaviours | 0.115 | 61 |
| risk_taking_behaviours | no_crisis | 0.273 | 11 |
| self-harm | anxiety_crisis | 0.050 | 20 |
| substance_abuse_or_withdrawal | no_crisis | 0.062 | 16 |
| suicidal_ideation | anxiety_crisis | 0.091 | 33 |
| violent_thoughts | suicidal_ideation | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.403 | 0.305 | 0.098 |
| no_crisis | risk_taking_behaviours | 0.387 | 0.115 | 0.273 |
| suicidal_ideation | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | suicidal_ideation | 0.242 | 0.182 | 0.061 |
| anxiety_crisis | suicidal_ideation | 0.142 | 0.051 | 0.091 |

### `H1_labeled_n206_s42.json` and `H4_labelled_n206_s42.json`:
	* 🟩 Agreement Rate: 57.77%
	* 🧠 Cohen's Kappa: 0.46
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `H4_labelled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |          41 |                        1 |           0 |                               1 |                   0 |                  1 |  0 |
| no_crisis                     |                4 |          47 |                        2 |           1 |                               0 |                   3 |                  4 |  0 |
| risk_taking_behaviours        |                1 |           3 |                        1 |           0 |                               0 |                   4 |                  2 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                4 |           2 |                        3 |           0 |                               0 |                  24 |                  0 |  0 |
| violent_thoughts              |                0 |           1 |                        0 |           1 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.760489 |                 0.107858 |    0        |                       0.0169492 |            0.121212 |          0.0169492 |  0 |
| no_crisis                     |        0.760489  |    0        |                 0.305514 |    0.166393 |                       0.0625    |            0.109786 |          0.23224   |  0 |
| risk_taking_behaviours        |        0.107858  |    0.305514 |                 0        |    0        |                       0         |            0.454545 |          0.181818  |  0 |
| self-harm                     |        0         |    0.166393 |                 0        |    0        |                       0.05      |            0.1      |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |    0.0625   |                 0        |    0.05     |                       0         |            0        |          0         |  0 |
| suicidal_ideation             |        0.121212  |    0.109786 |                 0.454545 |    0.1      |                       0         |            0        |          0.166667  |  0 |
| violent_thoughts              |        0.0169492 |    0.23224  |                 0.181818 |    0.166667 |                       0         |            0.166667 |          0         |  0 |
|                               |        0         |    0        |                 0        |    0        |                       0         |            0        |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.695 | 59 |
| no_crisis | anxiety_crisis | 0.066 | 61 |
| risk_taking_behaviours | suicidal_ideation | 0.364 | 11 |
| self-harm | no_crisis | 0.150 | 20 |
| substance_abuse_or_withdrawal | no_crisis | 0.062 | 16 |
| suicidal_ideation | anxiety_crisis | 0.121 | 33 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.760 | 0.695 | 0.066 |
| risk_taking_behaviours | suicidal_ideation | 0.455 | 0.364 | 0.091 |
| no_crisis | risk_taking_behaviours | 0.306 | 0.033 | 0.273 |
| no_crisis | violent_thoughts | 0.232 | 0.066 | 0.167 |
| risk_taking_behaviours | violent_thoughts | 0.182 | 0.182 | 0.000 |

### `H1_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json`:
	* 🟩 Agreement Rate: 73.30%
	* 🧠 Cohen's Kappa: 0.66
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               24 |          31 |                        0 |           0 |                               1 |                   2 |                  1 |  0 |
| no_crisis                     |                0 |          59 |                        0 |           0 |                               0 |                   2 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           8 |                        0 |           2 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          17 |                               1 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  31 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           2 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.525424  |                0         |    0        |                       0.0169492 |           0.0642013 |          0.0169492 |  0 |
| no_crisis                     |        0.525424  |   0         |                0.727273  |    0.05     |                       0         |           0.0630899 |          0         |  0 |
| risk_taking_behaviours        |        0         |   0.727273  |                0         |    0.181818 |                       0         |           0.0909091 |          0         |  0 |
| self-harm                     |        0         |   0.05      |                0.181818  |    0        |                       0.05      |           0.05      |          0.333333  |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |   0         |                0         |    0.05     |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0642013 |   0.0630899 |                0.0909091 |    0.05     |                       0         |           0         |          0         |  0 |
| violent_thoughts              |        0.0169492 |   0         |                0         |    0.333333 |                       0         |           0         |          0         |  0 |
|                               |        0         |   0         |                0         |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.525 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.727 | 11 |
| self-harm | no_crisis | 0.050 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation | anxiety_crisis | 0.030 | 33 |
| violent_thoughts | self-harm | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.727 | 0.000 | 0.727 |
| anxiety_crisis | no_crisis | 0.525 | 0.525 | 0.000 |
| self-harm | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | self-harm | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.091 | 0.091 | 0.000 |

### `H1_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json`:
	* 🟩 Agreement Rate: 71.84%
	* 🧠 Cohen's Kappa: 0.64
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               22 |          32 |                        0 |           0 |                               1 |                   3 |                  1 |  0 |
| no_crisis                     |                0 |          58 |                        0 |           0 |                               0 |                   2 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           9 |                        0 |           1 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          17 |                               1 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  31 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           1 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.542373  |                0         |   0         |                       0.0169492 |           0.0811505 |          0.0169492 |  0 |
| no_crisis                     |        0.542373  |   0         |                0.818182  |   0.05      |                       0         |           0.0630899 |          0         |  0 |
| risk_taking_behaviours        |        0         |   0.818182  |                0         |   0.0909091 |                       0         |           0.0909091 |          0         |  0 |
| self-harm                     |        0         |   0.05      |                0.0909091 |   0         |                       0.05      |           0.05      |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |   0         |                0         |   0.05      |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0811505 |   0.0630899 |                0.0909091 |   0.05      |                       0         |           0         |          0.166667  |  0 |
| violent_thoughts              |        0.0169492 |   0         |                0         |   0.166667  |                       0         |           0.166667  |          0         |  0 |
|                               |        0         |   0         |                0         |   0         |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.542 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.818 | 11 |
| self-harm | no_crisis | 0.050 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation | anxiety_crisis | 0.030 | 33 |
| violent_thoughts | self-harm | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.818 | 0.000 | 0.818 |
| anxiety_crisis | no_crisis | 0.542 | 0.542 | 0.000 |
| self-harm | violent_thoughts | 0.167 | 0.000 | 0.167 |
| suicidal_ideation | violent_thoughts | 0.167 | 0.000 | 0.167 |
| risk_taking_behaviours | self-harm | 0.091 | 0.091 | 0.000 |

### `H1_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 71.84%
	* 🧠 Cohen's Kappa: 0.64
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |          29 |                        0 |           0 |                               1 |                   3 |                  1 |  0 |
| no_crisis                     |                0 |          59 |                        0 |           0 |                               0 |                   2 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           8 |                        0 |           2 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          16 |                               1 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              14 |                   0 |                  0 |  2 |
| suicidal_ideation             |                2 |           1 |                        0 |           0 |                               0 |                  30 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           2 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.491525  |                0         |    0        |                       0.0169492 |           0.111454  |          0.0169492 |  0 |
| no_crisis                     |        0.491525  |   0         |                0.727273  |    0.1      |                       0         |           0.0630899 |          0         |  0 |
| risk_taking_behaviours        |        0         |   0.727273  |                0         |    0.181818 |                       0         |           0.0909091 |          0         |  0 |
| self-harm                     |        0         |   0.1       |                0.181818  |    0        |                       0.05      |           0.05      |          0.333333  |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |   0         |                0         |    0.05     |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.111454  |   0.0630899 |                0.0909091 |    0.05     |                       0         |           0         |          0         |  0 |
| violent_thoughts              |        0.0169492 |   0         |                0         |    0.333333 |                       0         |           0         |          0         |  0 |
|                               |        0         |   0         |                0         |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.492 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.727 | 11 |
| self-harm | no_crisis | 0.100 | 20 |
| substance_abuse_or_withdrawal |  | 0.125 | 16 |
| suicidal_ideation | anxiety_crisis | 0.061 | 33 |
| violent_thoughts | self-harm | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.727 | 0.000 | 0.727 |
| anxiety_crisis | no_crisis | 0.492 | 0.492 | 0.000 |
| self-harm | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | self-harm | 0.182 | 0.182 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.111 | 0.051 | 0.061 |

### `H1_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 70.87%
	* 🧠 Cohen's Kappa: 0.62
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               24 |          33 |                        0 |           0 |                               0 |                   2 |                  0 |  0 |
| no_crisis                     |                0 |          58 |                        0 |           0 |                               0 |                   2 |                  0 |  1 |
| risk_taking_behaviours        |                1 |           6 |                        0 |           2 |                               0 |                   2 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  31 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           1 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.559322  |                0.0909091 |    0        |                          0      |           0.0338983 |           0        |  0 |
| no_crisis                     |        0.559322  |   0         |                0.545455  |    0.15     |                          0.0625 |           0.0933929 |           0        |  0 |
| risk_taking_behaviours        |        0.0909091 |   0.545455  |                0         |    0.181818 |                          0      |           0.181818  |           0        |  0 |
| self-harm                     |        0         |   0.15      |                0.181818  |    0        |                          0.05   |           0.1       |           0.166667 |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0625    |                0         |    0.05     |                          0      |           0         |           0        |  0 |
| suicidal_ideation             |        0.0338983 |   0.0933929 |                0.181818  |    0.1      |                          0      |           0         |           0.166667 |  0 |
| violent_thoughts              |        0         |   0         |                0         |    0.166667 |                          0      |           0.166667  |           0        |  0 |
|                               |        0         |   0         |                0         |    0        |                          0      |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.559 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.545 | 11 |
| self-harm | no_crisis | 0.150 | 20 |
| substance_abuse_or_withdrawal | no_crisis | 0.062 | 16 |
| suicidal_ideation | no_crisis | 0.061 | 33 |
| violent_thoughts | self-harm | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.559 | 0.559 | 0.000 |
| no_crisis | risk_taking_behaviours | 0.545 | 0.000 | 0.545 |
| risk_taking_behaviours | self-harm | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.182 | 0.182 | 0.000 |
| self-harm | violent_thoughts | 0.167 | 0.000 | 0.167 |

### `H1_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 66.02%
	* 🧠 Cohen's Kappa: 0.56
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |          40 |                        0 |           0 |                               0 |                   2 |                  1 |  0 |
| no_crisis                     |                0 |          57 |                        0 |           0 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           6 |                        1 |           2 |                               0 |                   2 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           2 |                        0 |           0 |                               0 |                  30 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           1 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.677966  |                 0        |    0        |                       0         |           0.0642013 |          0.0169492 |  0 |
| no_crisis                     |        0.677966  |   0         |                 0.545455 |    0.15     |                       0.0788934 |           0.0933929 |          0.0163934 |  0 |
| risk_taking_behaviours        |        0         |   0.545455  |                 0        |    0.181818 |                       0         |           0.181818  |          0.166667  |  0 |
| self-harm                     |        0         |   0.15      |                 0.181818 |    0        |                       0.05      |           0.1       |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0788934 |                 0        |    0.05     |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0642013 |   0.0933929 |                 0.181818 |    0.1      |                       0         |           0         |          0.166667  |  0 |
| violent_thoughts              |        0.0169492 |   0.0163934 |                 0.166667 |    0.166667 |                       0         |           0.166667  |          0         |  0 |
|                               |        0         |   0         |                 0        |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.678 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.545 | 11 |
| self-harm | no_crisis | 0.150 | 20 |
| substance_abuse_or_withdrawal | no_crisis | 0.062 | 16 |
| suicidal_ideation | no_crisis | 0.061 | 33 |
| violent_thoughts | risk_taking_behaviours | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.678 | 0.678 | 0.000 |
| no_crisis | risk_taking_behaviours | 0.545 | 0.000 | 0.545 |
| risk_taking_behaviours | self-harm | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |

### `H1_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 66.50%
	* 🧠 Cohen's Kappa: 0.57
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |          42 |                        0 |           0 |                               0 |                   1 |                  1 |  0 |
| no_crisis                     |                0 |          57 |                        0 |           0 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           8 |                        1 |           1 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          15 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           3 |                        0 |           0 |                               0 |                  30 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           1 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.711864  |                0         |   0         |                       0         |           0.0169492 |          0.0169492 |  0 |
| no_crisis                     |        0.711864  |   0         |                0.727273  |   0.1       |                       0.0788934 |           0.123696  |          0.0163934 |  0 |
| risk_taking_behaviours        |        0         |   0.727273  |                0         |   0.0909091 |                       0         |           0.0909091 |          0         |  0 |
| self-harm                     |        0         |   0.1       |                0.0909091 |   0         |                       0.05      |           0.1       |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0788934 |                0         |   0.05      |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0169492 |   0.123696  |                0.0909091 |   0.1       |                       0         |           0         |          0.166667  |  0 |
| violent_thoughts              |        0.0169492 |   0.0163934 |                0         |   0.166667  |                       0         |           0.166667  |          0         |  0 |
|                               |        0         |   0         |                0         |   0         |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.712 | 59 |
| no_crisis | suicidal_ideation | 0.033 | 61 |
| risk_taking_behaviours | no_crisis | 0.727 | 11 |
| self-harm | no_crisis | 0.100 | 20 |
| substance_abuse_or_withdrawal | no_crisis | 0.062 | 16 |
| suicidal_ideation | no_crisis | 0.091 | 33 |
| violent_thoughts | self-harm | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.727 | 0.000 | 0.727 |
| anxiety_crisis | no_crisis | 0.712 | 0.712 | 0.000 |
| self-harm | violent_thoughts | 0.167 | 0.000 | 0.167 |
| suicidal_ideation | violent_thoughts | 0.167 | 0.000 | 0.167 |
| no_crisis | suicidal_ideation | 0.124 | 0.033 | 0.091 |

### `H1_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 67.48%
	* 🧠 Cohen's Kappa: 0.59
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               29 |          23 |                        0 |           0 |                               0 |                   6 |                  1 |  0 |
| no_crisis                     |                3 |          50 |                        0 |           0 |                               1 |                   3 |                  1 |  3 |
| risk_taking_behaviours        |                1 |           6 |                        0 |           1 |                               0 |                   2 |                  0 |  1 |
| self-harm                     |                0 |           2 |                        1 |          13 |                               2 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  28 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   2 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.439011  |                0.0909091 |    0        |                       0         |           0.131998  |          0.0169492 |  0 |
| no_crisis                     |        0.439011  |   0         |                0.545455  |    0.1      |                       0.0163934 |           0.0794834 |          0.0163934 |  0 |
| risk_taking_behaviours        |        0.0909091 |   0.545455  |                0         |    0.140909 |                       0         |           0.181818  |          0.166667  |  0 |
| self-harm                     |        0         |   0.1       |                0.140909  |    0        |                       0.1       |           0.1       |          0         |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0163934 |                0         |    0.1      |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.131998  |   0.0794834 |                0.181818  |    0.1      |                       0         |           0         |          0.333333  |  0 |
| violent_thoughts              |        0.0169492 |   0.0163934 |                0.166667  |    0        |                       0         |           0.333333  |          0         |  0 |
|                               |        0         |   0         |                0         |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.390 | 59 |
| no_crisis | anxiety_crisis | 0.049 | 61 |
| risk_taking_behaviours | no_crisis | 0.545 | 11 |
| self-harm | no_crisis | 0.100 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.091 | 33 |
| violent_thoughts | suicidal_ideation | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.545 | 0.000 | 0.545 |
| anxiety_crisis | no_crisis | 0.439 | 0.390 | 0.049 |
| suicidal_ideation | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | suicidal_ideation | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |

### `H1_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 68.93%
	* 🧠 Cohen's Kappa: 0.61
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               30 |          21 |                        0 |           0 |                               1 |                   6 |                  1 |  0 |
| no_crisis                     |                3 |          51 |                        0 |           0 |                               0 |                   3 |                  1 |  3 |
| risk_taking_behaviours        |                0 |           6 |                        0 |           1 |                               0 |                   3 |                  0 |  1 |
| self-harm                     |                0 |           1 |                        1 |          13 |                               2 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  29 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   2 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.405113  |                 0        |    0        |                       0.0169492 |           0.131998  |          0.0169492 |  0 |
| no_crisis                     |        0.405113  |   0         |                 0.545455 |    0.05     |                       0         |           0.0794834 |          0.0163934 |  0 |
| risk_taking_behaviours        |        0         |   0.545455  |                 0        |    0.140909 |                       0         |           0.272727  |          0.166667  |  0 |
| self-harm                     |        0         |   0.05      |                 0.140909 |    0        |                       0.1       |           0.15      |          0         |  0 |
| substance_abuse_or_withdrawal |        0.0169492 |   0         |                 0        |    0.1      |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.131998  |   0.0794834 |                 0.272727 |    0.15     |                       0         |           0         |          0.333333  |  0 |
| violent_thoughts              |        0.0169492 |   0.0163934 |                 0.166667 |    0        |                       0         |           0.333333  |          0         |  0 |
|                               |        0         |   0         |                 0        |    0        |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.356 | 59 |
| no_crisis | anxiety_crisis | 0.049 | 61 |
| risk_taking_behaviours | no_crisis | 0.545 | 11 |
| self-harm | suicidal_ideation | 0.150 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.061 | 33 |
| violent_thoughts | suicidal_ideation | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.545 | 0.000 | 0.545 |
| anxiety_crisis | no_crisis | 0.405 | 0.356 | 0.049 |
| suicidal_ideation | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | suicidal_ideation | 0.273 | 0.273 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |

### `H1_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 67.96%
	* 🧠 Cohen's Kappa: 0.59
Confusion Matrix between `H1_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               30 |          23 |                        0 |           0 |                               0 |                   5 |                  1 |  0 |
| no_crisis                     |                2 |          51 |                        0 |           0 |                               0 |                   3 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           7 |                        0 |           1 |                               0 |                   2 |                  0 |  1 |
| self-harm                     |                0 |           2 |                        1 |          13 |                               2 |                   1 |                  0 |  1 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  27 |                  0 |  4 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   2 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.422617  |                 0        |    0        |                             0   |           0.115049  |          0.0169492 |  0 |
| no_crisis                     |        0.422617  |   0         |                 0.636364 |    0.1      |                             0   |           0.0794834 |          0.0163934 |  0 |
| risk_taking_behaviours        |        0         |   0.636364  |                 0        |    0.140909 |                             0   |           0.181818  |          0.166667  |  0 |
| self-harm                     |        0         |   0.1       |                 0.140909 |    0        |                             0.1 |           0.05      |          0         |  0 |
| substance_abuse_or_withdrawal |        0         |   0         |                 0        |    0.1      |                             0   |           0         |          0         |  0 |
| suicidal_ideation             |        0.115049  |   0.0794834 |                 0.181818 |    0.05     |                             0   |           0         |          0.333333  |  0 |
| violent_thoughts              |        0.0169492 |   0.0163934 |                 0.166667 |    0        |                             0   |           0.333333  |          0         |  0 |
|                               |        0         |   0         |                 0        |    0        |                             0   |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.390 | 59 |
| no_crisis |  | 0.066 | 61 |
| risk_taking_behaviours | no_crisis | 0.636 | 11 |
| self-harm | no_crisis | 0.100 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.121 | 33 |
| violent_thoughts | suicidal_ideation | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.636 | 0.000 | 0.636 |
| anxiety_crisis | no_crisis | 0.423 | 0.390 | 0.033 |
| suicidal_ideation | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | suicidal_ideation | 0.182 | 0.182 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |

### `H2_labeled_n206_s42.json` and `H3_labeled_n206_s42.json`:
	* 🟩 Agreement Rate: 64.08%
	* 🧠 Cohen's Kappa: 0.53
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `H3_labeled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               18 |           2 |                        0 |           0 |                               1 |                   0 |                  0 |  0 |
| no_crisis                     |               25 |          60 |                       11 |           5 |                               3 |                   7 |                  2 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        2 |          12 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        1 |           0 |                              11 |                   0 |                  0 |  0 |
| suicidal_ideation             |                2 |           0 |                        2 |           1 |                               0 |                  28 |                  1 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   2 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.316477  |                0         |   0         |                        0.047619 |           0.0588235 |          0         |  0 |
| no_crisis                     |        0.316477  |   0         |                0.0973451 |   0.0442478 |                        0.103472 |           0.0619469 |          0.0176991 |  0 |
| risk_taking_behaviours        |        0         |   0.0973451 |                0         |   0.133333  |                        0.876923 |           0.258824  |          0         |  0 |
| self-harm                     |        0         |   0.0442478 |                0.133333  |   0         |                        0        |           0.0960784 |          0         |  0 |
| substance_abuse_or_withdrawal |        0.047619  |   0.103472  |                0.876923  |   0         |                        0        |           0         |          0         |  0 |
| suicidal_ideation             |        0.0588235 |   0.0619469 |                0.258824  |   0.0960784 |                        0        |           0         |          0.429412  |  0 |
| violent_thoughts              |        0         |   0.0176991 |                0         |   0         |                        0        |           0.429412  |          0         |  0 |
|                               |        0         |   0         |                0         |   0         |                        0        |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.095 | 21 |
| no_crisis | anxiety_crisis | 0.221 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | risk_taking_behaviours | 0.133 | 15 |
| substance_abuse_or_withdrawal | no_crisis | 0.077 | 13 |
| suicidal_ideation | anxiety_crisis | 0.059 | 34 |
| violent_thoughts | suicidal_ideation | 0.400 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.877 | 0.800 | 0.077 |
| suicidal_ideation | violent_thoughts | 0.429 | 0.029 | 0.400 |
| anxiety_crisis | no_crisis | 0.316 | 0.095 | 0.221 |
| risk_taking_behaviours | suicidal_ideation | 0.259 | 0.200 | 0.059 |
| risk_taking_behaviours | self-harm | 0.133 | 0.000 | 0.133 |

### `H2_labeled_n206_s42.json` and `H4_labelled_n206_s42.json`:
	* 🟩 Agreement Rate: 71.84%
	* 🧠 Cohen's Kappa: 0.59
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `H4_labelled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |          10 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               10 |          84 |                        4 |           3 |                               0 |                   6 |                  6 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               5 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          12 |                               0 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                3 |           2 |                        3 |           1 |                               0 |                  25 |                  0 |  0 |
| violent_thoughts              |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.564686  |                0         |   0         |                       0         |           0.0882353 |           0        |  0 |
| no_crisis                     |        0.564686  |   0         |                0.0353982 |   0.0265487 |                       0.0769231 |           0.111921  |           0.253097 |  0 |
| risk_taking_behaviours        |        0         |   0.0353982 |                0         |   0         |                       1         |           0.0882353 |           0        |  0 |
| self-harm                     |        0         |   0.0265487 |                0         |   0         |                       0         |           0.229412  |           0        |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0769231 |                1         |   0         |                       0         |           0         |           0        |  0 |
| suicidal_ideation             |        0.0882353 |   0.111921  |                0.0882353 |   0.229412  |                       0         |           0         |           0        |  0 |
| violent_thoughts              |        0         |   0.253097  |                0         |   0         |                       0         |           0         |           0        |  0 |
|                               |        0         |   0         |                0         |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.476 | 21 |
| no_crisis | anxiety_crisis | 0.088 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 1.000 | 5 |
| self-harm | suicidal_ideation | 0.200 | 15 |
| substance_abuse_or_withdrawal | no_crisis | 0.077 | 13 |
| suicidal_ideation | anxiety_crisis | 0.088 | 34 |
| violent_thoughts | no_crisis | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 1.000 | 1.000 | 0.000 |
| anxiety_crisis | no_crisis | 0.565 | 0.476 | 0.088 |
| no_crisis | violent_thoughts | 0.253 | 0.053 | 0.200 |
| self-harm | suicidal_ideation | 0.229 | 0.200 | 0.029 |
| no_crisis | suicidal_ideation | 0.112 | 0.053 | 0.059 |

### `H2_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json`:
	* 🟩 Agreement Rate: 85.44%
	* 🧠 Cohen's Kappa: 0.79
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               17 |           4 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                8 |          95 |                        0 |           4 |                               1 |                   5 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              13 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           2 |                               0 |                  31 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.261273   |                      0   |   0         |                      0          |           0         |                  0 |  0 |
| no_crisis                     |         0.261273 |  0          |                      0   |   0.0353982 |                      0.00884956 |           0.0736596 |                  0 |  0 |
| risk_taking_behaviours        |         0        |  0          |                      0   |   0         |                      0.8        |           0.2       |                  0 |  0 |
| self-harm                     |         0        |  0.0353982  |                      0   |   0         |                      0          |           0.0588235 |                  0 |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00884956 |                      0.8 |   0         |                      0          |           0         |                  0 |  0 |
| suicidal_ideation             |         0        |  0.0736596  |                      0.2 |   0.0588235 |                      0          |           0         |                  0 |  0 |
| violent_thoughts              |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |
|                               |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.190 | 21 |
| no_crisis | anxiety_crisis | 0.071 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | n/a | n/a | 15 |
| substance_abuse_or_withdrawal | n/a | n/a | 13 |
| suicidal_ideation | self-harm | 0.059 | 34 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| anxiety_crisis | no_crisis | 0.261 | 0.190 | 0.071 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| no_crisis | suicidal_ideation | 0.074 | 0.044 | 0.029 |
| self-harm | suicidal_ideation | 0.059 | 0.000 | 0.059 |

### `H2_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json`:
	* 🟩 Agreement Rate: 84.95%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |           4 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                7 |          95 |                        0 |           4 |                               1 |                   5 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              13 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           1 |                               0 |                  32 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.252423   |                      0   |   0         |                      0          |           0.047619  |                  0 |  0 |
| no_crisis                     |         0.252423 |  0          |                      0   |   0.102065  |                      0.00884956 |           0.0736596 |                  0 |  0 |
| risk_taking_behaviours        |         0        |  0          |                      0   |   0         |                      0.8        |           0.2       |                  0 |  0 |
| self-harm                     |         0        |  0.102065   |                      0   |   0         |                      0          |           0.0294118 |                  0 |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00884956 |                      0.8 |   0         |                      0          |           0         |                  0 |  0 |
| suicidal_ideation             |         0.047619 |  0.0736596  |                      0.2 |   0.0294118 |                      0          |           0         |                  0 |  0 |
| violent_thoughts              |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |
|                               |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.190 | 21 |
| no_crisis | anxiety_crisis | 0.062 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | no_crisis | 0.067 | 15 |
| substance_abuse_or_withdrawal | n/a | n/a | 13 |
| suicidal_ideation | no_crisis | 0.029 | 34 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| anxiety_crisis | no_crisis | 0.252 | 0.190 | 0.062 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| no_crisis | self-harm | 0.102 | 0.035 | 0.067 |
| no_crisis | suicidal_ideation | 0.074 | 0.044 | 0.029 |

### `H2_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 84.95%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               17 |           3 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |               10 |          95 |                        0 |           3 |                               1 |                   4 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               3 |                   1 |                  0 |  1 |
| self-harm                     |                0 |           0 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  1 |
| suicidal_ideation             |                0 |           1 |                        0 |           2 |                               0 |                  31 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.231353   |                      0   |   0         |                      0          |           0.047619  |                  0 |  0 |
| no_crisis                     |         0.231353 |  0          |                      0   |   0.0265487 |                      0.00884956 |           0.06481   |                  0 |  0 |
| risk_taking_behaviours        |         0        |  0          |                      0   |   0         |                      0.6        |           0.2       |                  0 |  0 |
| self-harm                     |         0        |  0.0265487  |                      0   |   0         |                      0          |           0.0588235 |                  0 |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00884956 |                      0.6 |   0         |                      0          |           0         |                  0 |  0 |
| suicidal_ideation             |         0.047619 |  0.06481    |                      0.2 |   0.0588235 |                      0          |           0         |                  0 |  0 |
| violent_thoughts              |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |
|                               |         0        |  0          |                      0   |   0         |                      0          |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.143 | 21 |
| no_crisis | anxiety_crisis | 0.088 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.600 | 5 |
| self-harm | n/a | n/a | 15 |
| substance_abuse_or_withdrawal |  | 0.077 | 13 |
| suicidal_ideation | self-harm | 0.059 | 34 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.600 | 0.600 | 0.000 |
| anxiety_crisis | no_crisis | 0.231 | 0.143 | 0.088 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| no_crisis | suicidal_ideation | 0.065 | 0.035 | 0.029 |
| self-harm | suicidal_ideation | 0.059 | 0.000 | 0.059 |

### `H2_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 85.44%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |           5 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                8 |          97 |                        0 |           1 |                               0 |                   6 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           1 |                               0 |                  32 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.308892   |                      0   |  0          |                       0.0769231 |           0         |                0   |  0 |
| no_crisis                     |        0.308892  |  0          |                      0   |  0.00884956 |                       0         |           0.0825091 |                0   |  0 |
| risk_taking_behaviours        |        0         |  0          |                      0   |  0          |                       0.8       |           0.2       |                0   |  0 |
| self-harm                     |        0         |  0.00884956 |                      0   |  0          |                       0         |           0.0294118 |                0   |  0 |
| substance_abuse_or_withdrawal |        0.0769231 |  0          |                      0.8 |  0          |                       0         |           0         |                0   |  0 |
| suicidal_ideation             |        0         |  0.0825091  |                      0.2 |  0.0294118  |                       0         |           0         |                0.2 |  0 |
| violent_thoughts              |        0         |  0          |                      0   |  0          |                       0         |           0.2       |                0   |  0 |
|                               |        0         |  0          |                      0   |  0          |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.238 | 21 |
| no_crisis | anxiety_crisis | 0.071 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | n/a | n/a | 15 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.077 | 13 |
| suicidal_ideation | no_crisis | 0.029 | 34 |
| violent_thoughts | suicidal_ideation | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| anxiety_crisis | no_crisis | 0.309 | 0.238 | 0.071 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| suicidal_ideation | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.083 | 0.053 | 0.029 |

### `H2_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 82.52%
	* 🧠 Cohen's Kappa: 0.73
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               10 |          11 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                6 |          97 |                        1 |           1 |                               1 |                   6 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           1 |                               0 |                  32 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.576907   |               0          |  0          |                      0.0769231  |           0         |         0          |  0 |
| no_crisis                     |        0.576907  |  0          |               0.00884956 |  0.00884956 |                      0.00884956 |           0.0825091 |         0.00884956 |  0 |
| risk_taking_behaviours        |        0         |  0.00884956 |               0          |  0          |                      0.8        |           0.2       |         0.2        |  0 |
| self-harm                     |        0         |  0.00884956 |               0          |  0          |                      0          |           0.0294118 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0769231 |  0.00884956 |               0.8        |  0          |                      0          |           0         |         0          |  0 |
| suicidal_ideation             |        0         |  0.0825091  |               0.2        |  0.0294118  |                      0          |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00884956 |               0.2        |  0          |                      0          |           0         |         0          |  0 |
|                               |        0         |  0          |               0          |  0          |                      0          |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.524 | 21 |
| no_crisis | anxiety_crisis | 0.053 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | n/a | n/a | 15 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.077 | 13 |
| suicidal_ideation | no_crisis | 0.029 | 34 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| anxiety_crisis | no_crisis | 0.577 | 0.524 | 0.053 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.083 | 0.053 | 0.029 |

### `H2_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 85.44%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |          10 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                3 |         102 |                        0 |           2 |                               1 |                   4 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           1 |                               0 |                  32 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.502739   |                0         |   0         |                      0.0769231  |           0         |         0          |  0 |
| no_crisis                     |        0.502739  |  0          |                0         |   0.0176991 |                      0.00884956 |           0.06481   |         0.00884956 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0666667 |                      0.8        |           0.2       |         0          |  0 |
| self-harm                     |        0         |  0.0176991  |                0.0666667 |   0         |                      0          |           0.0294118 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0769231 |  0.00884956 |                0.8       |   0         |                      0          |           0         |         0          |  0 |
| suicidal_ideation             |        0         |  0.06481    |                0.2       |   0.0294118 |                      0          |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00884956 |                0         |   0         |                      0          |           0         |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                      0          |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.476 | 21 |
| no_crisis | suicidal_ideation | 0.035 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | risk_taking_behaviours | 0.067 | 15 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.077 | 13 |
| suicidal_ideation | no_crisis | 0.029 | 34 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| anxiety_crisis | no_crisis | 0.503 | 0.476 | 0.027 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.077 | 0.000 | 0.077 |
| risk_taking_behaviours | self-harm | 0.067 | 0.000 | 0.067 |

### `H2_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 76.70%
	* 🧠 Cohen's Kappa: 0.68
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           0 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |               13 |          81 |                        0 |           3 |                               2 |                  10 |                  1 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          11 |                               1 |                   1 |                  0 |  1 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  30 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.115044   |                0         |   0         |                       0.0769231 |           0.047619  |         0          |  0 |
| no_crisis                     |        0.115044  |  0          |                0         |   0.0265487 |                       0.0176991 |           0.117907  |         0.00884956 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0666667 |                       0.8       |           0.2       |         0.2        |  0 |
| self-harm                     |        0         |  0.0265487  |                0.0666667 |   0         |                       0.0666667 |           0.0666667 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0769231 |  0.0176991  |                0.8       |   0.0666667 |                       0         |           0         |         0          |  0 |
| suicidal_ideation             |        0.047619  |  0.117907   |                0.2       |   0.0666667 |                       0         |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00884956 |                0.2       |   0         |                       0         |           0         |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                       0         |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | suicidal_ideation | 0.048 | 21 |
| no_crisis | anxiety_crisis | 0.115 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | risk_taking_behaviours | 0.067 | 15 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.077 | 13 |
| suicidal_ideation |  | 0.088 | 34 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.118 | 0.088 | 0.029 |
| anxiety_crisis | no_crisis | 0.115 | 0.000 | 0.115 |

### `H2_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 77.18%
	* 🧠 Cohen's Kappa: 0.68
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           0 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |               13 |          80 |                        0 |           3 |                               1 |                  11 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          11 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              13 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           0 |                        0 |           0 |                               0 |                  31 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.115044   |                0         |   0         |                      0          |           0.0770308 |         0          |  0 |
| no_crisis                     |        0.115044  |  0          |                0         |   0.0265487 |                      0.00884956 |           0.0973451 |         0.00884956 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0666667 |                      0.8        |           0.2       |         0.2        |  0 |
| self-harm                     |        0         |  0.0265487  |                0.0666667 |   0         |                      0.0666667  |           0.133333  |         0          |  0 |
| substance_abuse_or_withdrawal |        0         |  0.00884956 |                0.8       |   0.0666667 |                      0          |           0         |         0          |  0 |
| suicidal_ideation             |        0.0770308 |  0.0973451  |                0.2       |   0.133333  |                      0          |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00884956 |                0.2       |   0         |                      0          |           0         |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                      0          |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | suicidal_ideation | 0.048 | 21 |
| no_crisis | anxiety_crisis | 0.115 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | suicidal_ideation | 0.133 | 15 |
| substance_abuse_or_withdrawal | n/a | n/a | 13 |
| suicidal_ideation |  | 0.059 | 34 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.133 | 0.133 | 0.000 |
| anxiety_crisis | no_crisis | 0.115 | 0.000 | 0.115 |

### `H2_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 76.70%
	* 🧠 Cohen's Kappa: 0.67
Confusion Matrix between `H2_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               11 |          83 |                        0 |           3 |                               1 |                   9 |                  1 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               4 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          11 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              12 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           0 |                        0 |           0 |                               0 |                  28 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.144964   |                0         |   0         |                      0.0769231  |           0.0294118 |         0          |  0 |
| no_crisis                     |        0.144964  |  0          |                0         |   0.0265487 |                      0.00884956 |           0.079646  |         0.00884956 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0666667 |                      0.8        |           0.2       |         0.2        |  0 |
| self-harm                     |        0         |  0.0265487  |                0.0666667 |   0         |                      0.0666667  |           0.133333  |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0769231 |  0.00884956 |                0.8       |   0.0666667 |                      0          |           0         |         0          |  0 |
| suicidal_ideation             |        0.0294118 |  0.079646   |                0.2       |   0.133333  |                      0          |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00884956 |                0.2       |   0         |                      0          |           0         |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                      0          |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.048 | 21 |
| no_crisis | anxiety_crisis | 0.097 | 113 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 5 |
| self-harm | suicidal_ideation | 0.133 | 15 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.077 | 13 |
| suicidal_ideation |  | 0.147 | 34 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.800 | 0.800 | 0.000 |
| risk_taking_behaviours | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| anxiety_crisis | no_crisis | 0.145 | 0.048 | 0.097 |
| self-harm | suicidal_ideation | 0.133 | 0.133 | 0.000 |

### `H3_labeled_n206_s42.json` and `H4_labelled_n206_s42.json`:
	* 🟩 Agreement Rate: 66.50%
	* 🧠 Cohen's Kappa: 0.57
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `H4_labelled_n206_s42.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               18 |          26 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                2 |          57 |                        1 |           0 |                               0 |                   0 |                  3 |  0 |
| risk_taking_behaviours        |                0 |           7 |                        3 |           0 |                               1 |                   4 |                  1 |  0 |
| self-harm                     |                1 |           1 |                        0 |          14 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           4 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                3 |           2 |                        3 |           2 |                               1 |                  26 |                  2 |  0 |
| violent_thoughts              |                0 |           1 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.609524  |                 0        |   0.0555556 |                        0        |           0.0991453 |           0        |  0 |
| no_crisis                     |        0.609524  |   0         |                 0.453373 |   0.0555556 |                        0.210526 |           0.0512821 |           0.214286 |  0 |
| risk_taking_behaviours        |        0         |   0.453373  |                 0        |   0         |                        0.0625   |           0.326923  |           0.0625   |  0 |
| self-harm                     |        0.0555556 |   0.0555556 |                 0        |   0         |                        0        |           0.162393  |           0        |  0 |
| substance_abuse_or_withdrawal |        0         |   0.210526  |                 0.0625   |   0         |                        0        |           0.025641  |           0        |  0 |
| suicidal_ideation             |        0.0991453 |   0.0512821 |                 0.326923 |   0.162393  |                        0.025641 |           0         |           0.217949 |  0 |
| violent_thoughts              |        0         |   0.214286  |                 0.0625   |   0         |                        0        |           0.217949  |           0        |  0 |
|                               |        0         |   0         |                 0        |   0         |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.578 | 45 |
| no_crisis | violent_thoughts | 0.048 | 63 |
| risk_taking_behaviours | no_crisis | 0.438 | 16 |
| self-harm | suicidal_ideation | 0.111 | 18 |
| substance_abuse_or_withdrawal | no_crisis | 0.211 | 19 |
| suicidal_ideation | anxiety_crisis | 0.077 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.610 | 0.578 | 0.032 |
| no_crisis | risk_taking_behaviours | 0.453 | 0.016 | 0.438 |
| risk_taking_behaviours | suicidal_ideation | 0.327 | 0.250 | 0.077 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| no_crisis | violent_thoughts | 0.214 | 0.048 | 0.167 |

### `H3_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json`:
	* 🟩 Agreement Rate: 64.56%
	* 🧠 Cohen's Kappa: 0.54
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               18 |          23 |                        0 |           1 |                               0 |                   3 |                  0 |  0 |
| no_crisis                     |                5 |          54 |                        0 |           1 |                               2 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                0 |          10 |                        0 |           2 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                2 |           2 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  29 |                  2 |  0 |
| violent_thoughts              |                0 |           2 |                        0 |           1 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.590476 |                   0      |   0.0222222 |                        0.105263 |           0.0666667 |          0         |  0 |
| no_crisis                     |        0.590476  |    0        |                   0.625  |   0.18254   |                        0.137009 |           0.169719  |          0.333333  |  0 |
| risk_taking_behaviours        |        0         |    0.625    |                   0      |   0.125     |                        0.0625   |           0.1875    |          0         |  0 |
| self-harm                     |        0.0222222 |    0.18254  |                   0.125  |   0         |                        0        |           0.106838  |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0.105263  |    0.137009 |                   0.0625 |   0         |                        0        |           0         |          0         |  0 |
| suicidal_ideation             |        0.0666667 |    0.169719 |                   0.1875 |   0.106838  |                        0        |           0         |          0.0512821 |  0 |
| violent_thoughts              |        0         |    0.333333 |                   0      |   0.166667  |                        0        |           0.0512821 |          0         |  0 |
|                               |        0         |    0        |                   0      |   0         |                        0        |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.511 | 45 |
| no_crisis | anxiety_crisis | 0.079 | 63 |
| risk_taking_behaviours | no_crisis | 0.625 | 16 |
| self-harm | no_crisis | 0.167 | 18 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.105 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.625 | 0.000 | 0.625 |
| anxiety_crisis | no_crisis | 0.590 | 0.511 | 0.079 |
| no_crisis | violent_thoughts | 0.333 | 0.000 | 0.333 |
| risk_taking_behaviours | suicidal_ideation | 0.188 | 0.188 | 0.000 |
| no_crisis | self-harm | 0.183 | 0.016 | 0.167 |

### `H3_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json`:
	* 🟩 Agreement Rate: 63.59%
	* 🧠 Cohen's Kappa: 0.53
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               17 |          23 |                        0 |           1 |                               0 |                   4 |                  0 |  0 |
| no_crisis                     |                5 |          53 |                        0 |           1 |                               2 |                   1 |                  0 |  1 |
| risk_taking_behaviours        |                0 |          11 |                        0 |           1 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           3 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  29 |                  2 |  0 |
| violent_thoughts              |                0 |           2 |                        0 |           0 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.590476 |                   0      |   0.0222222 |                       0.0526316 |           0.0888889 |           0        |  0 |
| no_crisis                     |        0.590476  |    0        |                   0.6875 |   0.18254   |                       0.189641  |           0.169719  |           0.333333 |  0 |
| risk_taking_behaviours        |        0         |    0.6875   |                   0      |   0.0625    |                       0.0625    |           0.1875    |           0        |  0 |
| self-harm                     |        0.0222222 |    0.18254  |                   0.0625 |   0         |                       0         |           0.106838  |           0        |  0 |
| substance_abuse_or_withdrawal |        0.0526316 |    0.189641 |                   0.0625 |   0         |                       0         |           0         |           0        |  0 |
| suicidal_ideation             |        0.0888889 |    0.169719 |                   0.1875 |   0.106838  |                       0         |           0         |           0.217949 |  0 |
| violent_thoughts              |        0         |    0.333333 |                   0      |   0         |                       0         |           0.217949  |           0        |  0 |
|                               |        0         |    0        |                   0      |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.511 | 45 |
| no_crisis | anxiety_crisis | 0.079 | 63 |
| risk_taking_behaviours | no_crisis | 0.688 | 16 |
| self-harm | no_crisis | 0.167 | 18 |
| substance_abuse_or_withdrawal | no_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.688 | 0.000 | 0.688 |
| anxiety_crisis | no_crisis | 0.590 | 0.511 | 0.079 |
| no_crisis | violent_thoughts | 0.333 | 0.000 | 0.333 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| no_crisis | substance_abuse_or_withdrawal | 0.190 | 0.032 | 0.158 |

### `H3_labeled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 64.56%
	* 🧠 Cohen's Kappa: 0.54
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               21 |          20 |                        0 |           1 |                               0 |                   3 |                  0 |  0 |
| no_crisis                     |                5 |          54 |                        0 |           1 |                               2 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                0 |          10 |                        0 |           2 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           4 |                        0 |          13 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           3 |                        0 |           0 |                              13 |                   0 |                  0 |  2 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  29 |                  2 |  0 |
| violent_thoughts              |                0 |           2 |                        0 |           1 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.52381  |                   0      |   0.0222222 |                       0.0526316 |           0.0666667 |          0         |  0 |
| no_crisis                     |        0.52381   |    0        |                   0.625  |   0.238095  |                       0.189641  |           0.169719  |          0.333333  |  0 |
| risk_taking_behaviours        |        0         |    0.625    |                   0      |   0.125     |                       0.0625    |           0.1875    |          0         |  0 |
| self-harm                     |        0.0222222 |    0.238095 |                   0.125  |   0         |                       0         |           0.106838  |          0.166667  |  0 |
| substance_abuse_or_withdrawal |        0.0526316 |    0.189641 |                   0.0625 |   0         |                       0         |           0         |          0         |  0 |
| suicidal_ideation             |        0.0666667 |    0.169719 |                   0.1875 |   0.106838  |                       0         |           0         |          0.0512821 |  0 |
| violent_thoughts              |        0         |    0.333333 |                   0      |   0.166667  |                       0         |           0.0512821 |          0         |  0 |
|                               |        0         |    0        |                   0      |   0         |                       0         |           0         |          0         |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.444 | 45 |
| no_crisis | anxiety_crisis | 0.079 | 63 |
| risk_taking_behaviours | no_crisis | 0.625 | 16 |
| self-harm | no_crisis | 0.222 | 18 |
| substance_abuse_or_withdrawal | no_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.333 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.625 | 0.000 | 0.625 |
| anxiety_crisis | no_crisis | 0.524 | 0.444 | 0.079 |
| no_crisis | violent_thoughts | 0.333 | 0.000 | 0.333 |
| no_crisis | self-harm | 0.238 | 0.016 | 0.222 |
| no_crisis | substance_abuse_or_withdrawal | 0.190 | 0.032 | 0.158 |

### `H3_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 66.02%
	* 🧠 Cohen's Kappa: 0.56
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               17 |          24 |                        0 |           0 |                               0 |                   4 |                  0 |  0 |
| no_crisis                     |                4 |          58 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                2 |           8 |                        0 |           2 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           4 |                        0 |          13 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                2 |           2 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  30 |                  1 |  0 |
| violent_thoughts              |                0 |           1 |                        0 |           0 |                               0 |                   1 |                  3 |  1 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.596825 |                   0.125  |    0        |                        0.105263 |           0.0888889 |           0        |  0 |
| no_crisis                     |        0.596825  |    0        |                   0.5    |    0.222222 |                        0.105263 |           0.169719  |           0.166667 |  0 |
| risk_taking_behaviours        |        0.125     |    0.5      |                   0      |    0.125    |                        0.0625   |           0.1875    |           0        |  0 |
| self-harm                     |        0         |    0.222222 |                   0.125  |    0        |                        0        |           0.106838  |           0        |  0 |
| substance_abuse_or_withdrawal |        0.105263  |    0.105263 |                   0.0625 |    0        |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |        0.0888889 |    0.169719 |                   0.1875 |    0.106838 |                        0        |           0         |           0.192308 |  0 |
| violent_thoughts              |        0         |    0.166667 |                   0      |    0        |                        0        |           0.192308  |           0        |  0 |
|                               |        0         |    0        |                   0      |    0        |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.533 | 45 |
| no_crisis | anxiety_crisis | 0.063 | 63 |
| risk_taking_behaviours | no_crisis | 0.500 | 16 |
| self-harm | no_crisis | 0.222 | 18 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.105 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.597 | 0.533 | 0.063 |
| no_crisis | risk_taking_behaviours | 0.500 | 0.000 | 0.500 |
| no_crisis | self-harm | 0.222 | 0.000 | 0.222 |
| suicidal_ideation | violent_thoughts | 0.192 | 0.026 | 0.167 |
| risk_taking_behaviours | suicidal_ideation | 0.188 | 0.188 | 0.000 |

### `H3_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 62.62%
	* 🧠 Cohen's Kappa: 0.51
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               12 |          29 |                        0 |           0 |                               0 |                   4 |                  0 |  0 |
| no_crisis                     |                5 |          56 |                        1 |           0 |                               0 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                0 |          10 |                        0 |           2 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           4 |                        0 |          13 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           3 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  29 |                  2 |  0 |
| violent_thoughts              |                0 |           1 |                        1 |           0 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.72381  |                 0        |    0        |                        0        |           0.0888889 |           0        |  0 |
| no_crisis                     |        0.72381   |    0        |                 0.640873 |    0.222222 |                        0.157895 |           0.169719  |           0.166667 |  0 |
| risk_taking_behaviours        |        0         |    0.640873 |                 0        |    0.125    |                        0.0625   |           0.1875    |           0.166667 |  0 |
| self-harm                     |        0         |    0.222222 |                 0.125    |    0        |                        0        |           0.106838  |           0        |  0 |
| substance_abuse_or_withdrawal |        0         |    0.157895 |                 0.0625   |    0        |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |        0.0888889 |    0.169719 |                 0.1875   |    0.106838 |                        0        |           0         |           0.217949 |  0 |
| violent_thoughts              |        0         |    0.166667 |                 0.166667 |    0        |                        0        |           0.217949  |           0        |  0 |
|                               |        0         |    0        |                 0        |    0        |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.644 | 45 |
| no_crisis | anxiety_crisis | 0.079 | 63 |
| risk_taking_behaviours | no_crisis | 0.625 | 16 |
| self-harm | no_crisis | 0.222 | 18 |
| substance_abuse_or_withdrawal | no_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.724 | 0.644 | 0.079 |
| no_crisis | risk_taking_behaviours | 0.641 | 0.016 | 0.625 |
| no_crisis | self-harm | 0.222 | 0.000 | 0.222 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| risk_taking_behaviours | suicidal_ideation | 0.188 | 0.188 | 0.000 |

### `H3_labeled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 64.56%
	* 🧠 Cohen's Kappa: 0.54
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |          32 |                        0 |           0 |                               0 |                   2 |                  0 |  0 |
| no_crisis                     |                4 |          58 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                0 |          10 |                        1 |           1 |                               1 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        0 |          14 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           3 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           6 |                        0 |           2 |                               0 |                  29 |                  2 |  0 |
| violent_thoughts              |                0 |           1 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.774603 |                   0      |    0        |                        0        |           0.0444444 |           0        |  0 |
| no_crisis                     |        0.774603  |    0        |                   0.625  |    0.166667 |                        0.157895 |           0.169719  |           0.166667 |  0 |
| risk_taking_behaviours        |        0         |    0.625    |                   0      |    0.0625   |                        0.0625   |           0.1875    |           0        |  0 |
| self-harm                     |        0         |    0.166667 |                   0.0625 |    0        |                        0        |           0.106838  |           0        |  0 |
| substance_abuse_or_withdrawal |        0         |    0.157895 |                   0.0625 |    0        |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |        0.0444444 |    0.169719 |                   0.1875 |    0.106838 |                        0        |           0         |           0.217949 |  0 |
| violent_thoughts              |        0         |    0.166667 |                   0      |    0        |                        0        |           0.217949  |           0        |  0 |
|                               |        0         |    0        |                   0      |    0        |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.711 | 45 |
| no_crisis | anxiety_crisis | 0.063 | 63 |
| risk_taking_behaviours | no_crisis | 0.625 | 16 |
| self-harm | no_crisis | 0.167 | 18 |
| substance_abuse_or_withdrawal | no_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.154 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.775 | 0.711 | 0.063 |
| no_crisis | risk_taking_behaviours | 0.625 | 0.000 | 0.625 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| risk_taking_behaviours | suicidal_ideation | 0.188 | 0.188 | 0.000 |
| no_crisis | suicidal_ideation | 0.170 | 0.016 | 0.154 |

### `H3_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 61.65%
	* 🧠 Cohen's Kappa: 0.51
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               21 |          13 |                        0 |           1 |                               0 |                   9 |                  0 |  1 |
| no_crisis                     |               10 |          50 |                        0 |           0 |                               2 |                   0 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           9 |                        0 |           1 |                               1 |                   4 |                  0 |  1 |
| self-harm                     |                0 |           3 |                        1 |          11 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                3 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           5 |                        0 |           1 |                               0 |                  27 |                  2 |  4 |
| violent_thoughts              |                0 |           1 |                        1 |           0 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.447619  |                 0        |   0.0222222 |                       0.157895  |            0.2      |           0        |  0 |
| no_crisis                     |        0.447619  |   0         |                 0.5625   |   0.166667  |                       0.0843776 |            0.128205 |           0.166667 |  0 |
| risk_taking_behaviours        |        0         |   0.5625    |                 0        |   0.118056  |                       0.0625    |            0.25     |           0.166667 |  0 |
| self-harm                     |        0.0222222 |   0.166667  |                 0.118056 |   0         |                       0.0555556 |            0.136752 |           0        |  0 |
| substance_abuse_or_withdrawal |        0.157895  |   0.0843776 |                 0.0625   |   0.0555556 |                       0         |            0        |           0        |  0 |
| suicidal_ideation             |        0.2       |   0.128205  |                 0.25     |   0.136752  |                       0         |            0        |           0.217949 |  0 |
| violent_thoughts              |        0         |   0.166667  |                 0.166667 |   0         |                       0         |            0.217949 |           0        |  0 |
|                               |        0         |   0         |                 0        |   0         |                       0         |            0        |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.289 | 45 |
| no_crisis | anxiety_crisis | 0.159 | 63 |
| risk_taking_behaviours | no_crisis | 0.562 | 16 |
| self-harm | no_crisis | 0.167 | 18 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.128 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.562 | 0.000 | 0.562 |
| anxiety_crisis | no_crisis | 0.448 | 0.289 | 0.159 |
| risk_taking_behaviours | suicidal_ideation | 0.250 | 0.250 | 0.000 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| anxiety_crisis | suicidal_ideation | 0.200 | 0.200 | 0.000 |

### `H3_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 62.62%
	* 🧠 Cohen's Kappa: 0.53
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               22 |          13 |                        0 |           1 |                               0 |                   9 |                  0 |  0 |
| no_crisis                     |                8 |          50 |                        0 |           0 |                               2 |                   1 |                  0 |  2 |
| risk_taking_behaviours        |                0 |           9 |                        0 |           1 |                               1 |                   5 |                  0 |  0 |
| self-harm                     |                0 |           3 |                        1 |          11 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                3 |           0 |                        0 |           0 |                              15 |                   0 |                  0 |  1 |
| suicidal_ideation             |                1 |           4 |                        0 |           1 |                               0 |                  28 |                  2 |  3 |
| violent_thoughts              |                0 |           1 |                        1 |           0 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.415873 |                 0        |   0.0222222 |                       0.157895  |            0.225641 |           0        |  0 |
| no_crisis                     |        0.415873  |    0        |                 0.5625   |   0.166667  |                       0.031746  |            0.118437 |           0.166667 |  0 |
| risk_taking_behaviours        |        0         |    0.5625   |                 0        |   0.118056  |                       0.0625    |            0.3125   |           0.166667 |  0 |
| self-harm                     |        0.0222222 |    0.166667 |                 0.118056 |   0         |                       0.0555556 |            0.136752 |           0        |  0 |
| substance_abuse_or_withdrawal |        0.157895  |    0.031746 |                 0.0625   |   0.0555556 |                       0         |            0        |           0        |  0 |
| suicidal_ideation             |        0.225641  |    0.118437 |                 0.3125   |   0.136752  |                       0         |            0        |           0.217949 |  0 |
| violent_thoughts              |        0         |    0.166667 |                 0.166667 |   0         |                       0         |            0.217949 |           0        |  0 |
|                               |        0         |    0        |                 0        |   0         |                       0         |            0        |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.289 | 45 |
| no_crisis | anxiety_crisis | 0.127 | 63 |
| risk_taking_behaviours | no_crisis | 0.562 | 16 |
| self-harm | no_crisis | 0.167 | 18 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.103 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.562 | 0.000 | 0.562 |
| anxiety_crisis | no_crisis | 0.416 | 0.289 | 0.127 |
| risk_taking_behaviours | suicidal_ideation | 0.312 | 0.312 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.226 | 0.200 | 0.026 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |

### `H3_labeled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 61.65%
	* 🧠 Cohen's Kappa: 0.51
Confusion Matrix between `H3_labeled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               21 |          16 |                        0 |           1 |                               0 |                   7 |                  0 |  0 |
| no_crisis                     |                8 |          51 |                        0 |           0 |                               1 |                   0 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           8 |                        0 |           1 |                               1 |                   5 |                  0 |  1 |
| self-harm                     |                0 |           2 |                        1 |          11 |                               1 |                   1 |                  0 |  2 |
| substance_abuse_or_withdrawal |                3 |           1 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           5 |                        0 |           1 |                               0 |                  26 |                  2 |  4 |
| violent_thoughts              |                0 |           1 |                        1 |           0 |                               0 |                   1 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.48254   |                 0        |   0.0222222 |                       0.157895  |           0.181197  |           0        |  0 |
| no_crisis                     |        0.48254   |   0         |                 0.5      |   0.111111  |                       0.0685046 |           0.128205  |           0.166667 |  0 |
| risk_taking_behaviours        |        0         |   0.5       |                 0        |   0.118056  |                       0.0625    |           0.3125    |           0.166667 |  0 |
| self-harm                     |        0.0222222 |   0.111111  |                 0.118056 |   0         |                       0.0555556 |           0.0811966 |           0        |  0 |
| substance_abuse_or_withdrawal |        0.157895  |   0.0685046 |                 0.0625   |   0.0555556 |                       0         |           0         |           0        |  0 |
| suicidal_ideation             |        0.181197  |   0.128205  |                 0.3125   |   0.0811966 |                       0         |           0         |           0.217949 |  0 |
| violent_thoughts              |        0         |   0.166667  |                 0.166667 |   0         |                       0         |           0.217949  |           0        |  0 |
|                               |        0         |   0         |                 0        |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.356 | 45 |
| no_crisis | anxiety_crisis | 0.127 | 63 |
| risk_taking_behaviours | no_crisis | 0.500 | 16 |
| self-harm | no_crisis | 0.111 | 18 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.158 | 19 |
| suicidal_ideation | no_crisis | 0.128 | 39 |
| violent_thoughts | no_crisis | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.500 | 0.000 | 0.500 |
| anxiety_crisis | no_crisis | 0.483 | 0.356 | 0.127 |
| risk_taking_behaviours | suicidal_ideation | 0.312 | 0.312 | 0.000 |
| suicidal_ideation | violent_thoughts | 0.218 | 0.051 | 0.167 |
| anxiety_crisis | suicidal_ideation | 0.181 | 0.156 | 0.026 |

### `H4_labelled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json`:
	* 🟩 Agreement Rate: 73.30%
	* 🧠 Cohen's Kappa: 0.62
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               12 |           7 |                        0 |           0 |                               0 |                   5 |                  0 |  0 |
| no_crisis                     |               13 |          78 |                        0 |           2 |                               2 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           4 |                               0 |                  26 |                  0 |  0 |
| violent_thoughts              |                0 |           6 |                        0 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.42432   |                 0        |   0         |                       0         |           0.208333  |           0        |  0 |
| no_crisis                     |         0.42432  |   0         |                 0.571429 |   0.0829082 |                       0.0204082 |           0.138055  |           0.610204 |  0 |
| risk_taking_behaviours        |         0        |   0.571429  |                 0        |   0         |                       0         |           0.428571  |           0        |  0 |
| self-harm                     |         0        |   0.0829082 |                 0        |   0         |                       0         |           0.117647  |           0        |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0204082 |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| suicidal_ideation             |         0.208333 |   0.138055  |                 0.428571 |   0.117647  |                       0.0588235 |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.610204  |                 0        |   0         |                       0         |           0         |           0        |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.292 | 24 |
| no_crisis | anxiety_crisis | 0.133 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | no_crisis | 0.062 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.600 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | violent_thoughts | 0.610 | 0.010 | 0.600 |
| no_crisis | risk_taking_behaviours | 0.571 | 0.000 | 0.571 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | no_crisis | 0.424 | 0.292 | 0.133 |
| anxiety_crisis | suicidal_ideation | 0.208 | 0.208 | 0.000 |

### `H4_labelled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json`:
	* 🟩 Agreement Rate: 73.30%
	* 🧠 Cohen's Kappa: 0.62
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |           7 |                        0 |           0 |                               0 |                   6 |                  0 |  0 |
| no_crisis                     |               12 |          78 |                        0 |           2 |                               2 |                   2 |                  1 |  1 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           5 |                        0 |           2 |                               0 |                  27 |                  0 |  0 |
| violent_thoughts              |                0 |           6 |                        0 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.414116  |                 0        |   0         |                       0         |           0.25      |           0        |  0 |
| no_crisis                     |         0.414116 |   0         |                 0.571429 |   0.0829082 |                       0.0204082 |           0.167467  |           0.610204 |  0 |
| risk_taking_behaviours        |         0        |   0.571429  |                 0        |   0         |                       0         |           0.428571  |           0        |  0 |
| self-harm                     |         0        |   0.0829082 |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0204082 |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| suicidal_ideation             |         0.25     |   0.167467  |                 0.428571 |   0.0588235 |                       0.0588235 |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.610204  |                 0        |   0         |                       0         |           0         |           0        |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.292 | 24 |
| no_crisis | anxiety_crisis | 0.122 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | no_crisis | 0.062 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.147 | 34 |
| violent_thoughts | no_crisis | 0.600 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | violent_thoughts | 0.610 | 0.010 | 0.600 |
| no_crisis | risk_taking_behaviours | 0.571 | 0.000 | 0.571 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | no_crisis | 0.414 | 0.292 | 0.122 |
| anxiety_crisis | suicidal_ideation | 0.250 | 0.250 | 0.000 |

### `H4_labelled_n206_s42.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 71.84%
	* 🧠 Cohen's Kappa: 0.60
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               13 |           6 |                        0 |           0 |                               0 |                   5 |                  0 |  0 |
| no_crisis                     |               14 |          77 |                        0 |           2 |                               2 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              14 |                   1 |                  0 |  2 |
| suicidal_ideation             |                0 |           4 |                        0 |           4 |                               0 |                  26 |                  0 |  0 |
| violent_thoughts              |                0 |           6 |                        0 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.392857  |                 0        |    0        |                       0         |           0.208333  |           0        |  0 |
| no_crisis                     |         0.392857 |   0         |                 0.571429 |    0.145408 |                       0.0204082 |           0.138055  |           0.610204 |  0 |
| risk_taking_behaviours        |         0        |   0.571429  |                 0        |    0        |                       0         |           0.428571  |           0        |  0 |
| self-harm                     |         0        |   0.145408  |                 0        |    0        |                       0         |           0.117647  |           0        |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0204082 |                 0        |    0        |                       0         |           0.0588235 |           0        |  0 |
| suicidal_ideation             |         0.208333 |   0.138055  |                 0.428571 |    0.117647 |                       0.0588235 |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.610204  |                 0        |    0        |                       0         |           0         |           0        |  0 |
|                               |         0        |   0         |                 0        |    0        |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.250 | 24 |
| no_crisis | anxiety_crisis | 0.143 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | no_crisis | 0.125 | 16 |
| substance_abuse_or_withdrawal |  | 0.118 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.600 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | violent_thoughts | 0.610 | 0.010 | 0.600 |
| no_crisis | risk_taking_behaviours | 0.571 | 0.000 | 0.571 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | no_crisis | 0.393 | 0.250 | 0.143 |
| anxiety_crisis | suicidal_ideation | 0.208 | 0.208 | 0.000 |

### `H4_labelled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 74.27%
	* 🧠 Cohen's Kappa: 0.63
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |           7 |                        0 |           0 |                               0 |                   6 |                  0 |  0 |
| no_crisis                     |               13 |          82 |                        0 |           0 |                               0 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                1 |           3 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           3 |                               0 |                  27 |                  0 |  0 |
| violent_thoughts              |                0 |           5 |                        0 |           0 |                               0 |                   1 |                  3 |  1 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |    0.42432  |                 0.142857 |   0         |                       0         |           0.25      |           0        |  0 |
| no_crisis                     |         0.42432  |    0        |                 0.428571 |   0.125     |                       0         |           0.138055  |           0.510204 |  0 |
| risk_taking_behaviours        |         0.142857 |    0.428571 |                 0        |   0         |                       0         |           0.428571  |           0        |  0 |
| self-harm                     |         0        |    0.125    |                 0        |   0         |                       0         |           0.0882353 |           0        |  0 |
| substance_abuse_or_withdrawal |         0        |    0        |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| suicidal_ideation             |         0.25     |    0.138055 |                 0.428571 |   0.0882353 |                       0.0588235 |           0         |           0.1      |  0 |
| violent_thoughts              |         0        |    0.510204 |                 0        |   0         |                       0         |           0.1       |           0        |  0 |
|                               |         0        |    0        |                 0        |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.292 | 24 |
| no_crisis | anxiety_crisis | 0.133 | 98 |
| risk_taking_behaviours | no_crisis | 0.429 | 7 |
| self-harm | no_crisis | 0.125 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.500 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | violent_thoughts | 0.510 | 0.010 | 0.500 |
| no_crisis | risk_taking_behaviours | 0.429 | 0.000 | 0.429 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | no_crisis | 0.424 | 0.292 | 0.133 |
| anxiety_crisis | suicidal_ideation | 0.250 | 0.250 | 0.000 |

### `H4_labelled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 73.79%
	* 🧠 Cohen's Kappa: 0.62
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |                7 |          11 |                        0 |           0 |                               0 |                   6 |                  0 |  0 |
| no_crisis                     |               10 |          83 |                        2 |           0 |                               1 |                   2 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           3 |                               0 |                  27 |                  0 |  0 |
| violent_thoughts              |                0 |           5 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.560374  |                 0        |   0         |                       0         |           0.25      |                0   |  0 |
| no_crisis                     |         0.560374 |   0         |                 0.591837 |   0.125     |                       0.0102041 |           0.138055  |                0.5 |  0 |
| risk_taking_behaviours        |         0        |   0.591837  |                 0        |   0         |                       0         |           0.428571  |                0   |  0 |
| self-harm                     |         0        |   0.125     |                 0        |   0         |                       0         |           0.0882353 |                0   |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0102041 |                 0        |   0         |                       0         |           0.0588235 |                0   |  0 |
| suicidal_ideation             |         0.25     |   0.138055  |                 0.428571 |   0.0882353 |                       0.0588235 |           0         |                0   |  0 |
| violent_thoughts              |         0        |   0.5       |                 0        |   0         |                       0         |           0         |                0   |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.458 | 24 |
| no_crisis | anxiety_crisis | 0.102 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | no_crisis | 0.125 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.500 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.592 | 0.020 | 0.571 |
| anxiety_crisis | no_crisis | 0.560 | 0.458 | 0.102 |
| no_crisis | violent_thoughts | 0.500 | 0.000 | 0.500 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.250 | 0.250 | 0.000 |

### `H4_labelled_n206_s42.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 76.70%
	* 🧠 Cohen's Kappa: 0.66
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |                8 |          12 |                        0 |           0 |                               0 |                   4 |                  0 |  0 |
| no_crisis                     |                7 |          87 |                        0 |           0 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          15 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        1 |           2 |                               0 |                  27 |                  0 |  0 |
| violent_thoughts              |                0 |           5 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.571429  |                 0        |   0         |                       0         |           0.166667  |           0        |  0 |
| no_crisis                     |         0.571429 |   0         |                 0.571429 |   0.0625    |                       0.0102041 |           0.138055  |           0.510204 |  0 |
| risk_taking_behaviours        |         0        |   0.571429  |                 0        |   0         |                       0         |           0.457983  |           0        |  0 |
| self-harm                     |         0        |   0.0625    |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0102041 |                 0        |   0         |                       0         |           0.0588235 |           0        |  0 |
| suicidal_ideation             |         0.166667 |   0.138055  |                 0.457983 |   0.0588235 |                       0.0588235 |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.510204  |                 0        |   0         |                       0         |           0         |           0        |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.500 | 24 |
| no_crisis | anxiety_crisis | 0.071 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | no_crisis | 0.062 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.500 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.571 | 0.500 | 0.071 |
| no_crisis | risk_taking_behaviours | 0.571 | 0.000 | 0.571 |
| no_crisis | violent_thoughts | 0.510 | 0.010 | 0.500 |
| risk_taking_behaviours | suicidal_ideation | 0.458 | 0.429 | 0.029 |
| anxiety_crisis | suicidal_ideation | 0.167 | 0.167 | 0.000 |

### `H4_labelled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 65.53%
	* 🧠 Cohen's Kappa: 0.54
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               12 |           4 |                        0 |           0 |                               0 |                   7 |                  0 |  1 |
| no_crisis                     |               22 |          65 |                        1 |           1 |                               1 |                   5 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          12 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           1 |                               1 |                  25 |                  0 |  3 |
| violent_thoughts              |                0 |           4 |                        0 |           0 |                               1 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.391156  |                 0        |   0         |                       0         |           0.291667  |                0   |  0 |
| no_crisis                     |         0.391156 |   0         |                 0.581633 |   0.0727041 |                       0.0102041 |           0.168667  |                0.4 |  0 |
| risk_taking_behaviours        |         0        |   0.581633  |                 0        |   0.0625    |                       0         |           0.428571  |                0   |  0 |
| self-harm                     |         0        |   0.0727041 |                 0.0625   |   0         |                       0         |           0.154412  |                0   |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0102041 |                 0        |   0         |                       0         |           0.0882353 |                0.1 |  0 |
| suicidal_ideation             |         0.291667 |   0.168667  |                 0.428571 |   0.154412  |                       0.0882353 |           0         |                0   |  0 |
| violent_thoughts              |         0        |   0.4       |                 0        |   0         |                       0.1       |           0         |                0   |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | suicidal_ideation | 0.292 | 24 |
| no_crisis | anxiety_crisis | 0.224 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | suicidal_ideation | 0.125 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.400 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.582 | 0.010 | 0.571 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| no_crisis | violent_thoughts | 0.400 | 0.000 | 0.400 |
| anxiety_crisis | no_crisis | 0.391 | 0.167 | 0.224 |
| anxiety_crisis | suicidal_ideation | 0.292 | 0.292 | 0.000 |

### `H4_labelled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 65.05%
	* 🧠 Cohen's Kappa: 0.53
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               12 |           4 |                        0 |           0 |                               0 |                   8 |                  0 |  0 |
| no_crisis                     |               22 |          63 |                        1 |           1 |                               2 |                   6 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           4 |                        0 |           0 |                               0 |                   3 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          12 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           3 |                        0 |           1 |                               1 |                  26 |                  0 |  3 |
| violent_thoughts              |                0 |           5 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.391156  |                 0        |   0         |                       0         |           0.333333  |                0   |  0 |
| no_crisis                     |         0.391156 |   0         |                 0.581633 |   0.0727041 |                       0.0204082 |           0.14946   |                0.5 |  0 |
| risk_taking_behaviours        |         0        |   0.581633  |                 0        |   0.0625    |                       0         |           0.428571  |                0   |  0 |
| self-harm                     |         0        |   0.0727041 |                 0.0625   |   0         |                       0         |           0.154412  |                0   |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0204082 |                 0        |   0         |                       0         |           0.0882353 |                0   |  0 |
| suicidal_ideation             |         0.333333 |   0.14946   |                 0.428571 |   0.154412  |                       0.0882353 |           0         |                0   |  0 |
| violent_thoughts              |         0        |   0.5       |                 0        |   0         |                       0         |           0         |                0   |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | suicidal_ideation | 0.333 | 24 |
| no_crisis | anxiety_crisis | 0.224 | 98 |
| risk_taking_behaviours | no_crisis | 0.571 | 7 |
| self-harm | suicidal_ideation | 0.125 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.088 | 34 |
| violent_thoughts | no_crisis | 0.500 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.582 | 0.010 | 0.571 |
| no_crisis | violent_thoughts | 0.500 | 0.000 | 0.500 |
| risk_taking_behaviours | suicidal_ideation | 0.429 | 0.429 | 0.000 |
| anxiety_crisis | no_crisis | 0.391 | 0.167 | 0.224 |
| anxiety_crisis | suicidal_ideation | 0.333 | 0.333 | 0.000 |

### `H4_labelled_n206_s42.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 65.53%
	* 🧠 Cohen's Kappa: 0.54
Confusion Matrix between `H4_labelled_n206_s42.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               12 |           6 |                        0 |           0 |                               0 |                   6 |                  0 |  0 |
| no_crisis                     |               21 |          66 |                        1 |           1 |                               1 |                   5 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           3 |                        0 |           0 |                               0 |                   2 |                  0 |  2 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               0 |                   2 |                  0 |  1 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   1 |                  0 |  0 |
| suicidal_ideation             |                0 |           4 |                        0 |           1 |                               1 |                  24 |                  0 |  4 |
| violent_thoughts              |                0 |           5 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.464286  |                 0        |   0         |                       0         |           0.25      |                0   |  0 |
| no_crisis                     |         0.464286 |   0         |                 0.438776 |   0.0102041 |                       0.0102041 |           0.168667  |                0.5 |  0 |
| risk_taking_behaviours        |         0        |   0.438776  |                 0        |   0.0625    |                       0         |           0.285714  |                0   |  0 |
| self-harm                     |         0        |   0.0102041 |                 0.0625   |   0         |                       0         |           0.154412  |                0   |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0102041 |                 0        |   0         |                       0         |           0.0882353 |                0   |  0 |
| suicidal_ideation             |         0.25     |   0.168667  |                 0.285714 |   0.154412  |                       0.0882353 |           0         |                0   |  0 |
| violent_thoughts              |         0        |   0.5       |                 0        |   0         |                       0         |           0         |                0   |  0 |
|                               |         0        |   0         |                 0        |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.250 | 24 |
| no_crisis | anxiety_crisis | 0.214 | 98 |
| risk_taking_behaviours | no_crisis | 0.429 | 7 |
| self-harm | suicidal_ideation | 0.125 | 16 |
| substance_abuse_or_withdrawal | suicidal_ideation | 0.059 | 17 |
| suicidal_ideation | no_crisis | 0.118 | 34 |
| violent_thoughts | no_crisis | 0.500 | 10 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | violent_thoughts | 0.500 | 0.000 | 0.500 |
| anxiety_crisis | no_crisis | 0.464 | 0.250 | 0.214 |
| no_crisis | risk_taking_behaviours | 0.439 | 0.010 | 0.429 |
| risk_taking_behaviours | suicidal_ideation | 0.286 | 0.286 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.250 | 0.250 | 0.000 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json`:
	* 🟩 Agreement Rate: 97.09%
	* 🧠 Cohen's Kappa: 0.96
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               23 |           2 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                0 |          98 |                        0 |           0 |                               0 |                   1 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          19 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           0 |                        0 |           0 |                               0 |                  37 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |             0    |    0.08     |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| no_crisis                     |             0.08 |    0        |                        0 |    0.047619 |                               0 |            0.01     |                  0 |  0 |
| risk_taking_behaviours        |             0    |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| self-harm                     |             0    |    0.047619 |                        0 |    0        |                               0 |            0.047619 |                  0 |  0 |
| substance_abuse_or_withdrawal |             0    |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| suicidal_ideation             |             0    |    0.01     |                        0 |    0.047619 |                               0 |            0        |                  0 |  0 |
| violent_thoughts              |             0    |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
|                               |             0    |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.080 | 25 |
| no_crisis | suicidal_ideation | 0.010 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.048 | 21 |
| substance_abuse_or_withdrawal | n/a | n/a | 18 |
| suicidal_ideation | n/a | n/a | 37 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.080 | 0.080 | 0.000 |
| no_crisis | self-harm | 0.048 | 0.000 | 0.048 |
| self-harm | suicidal_ideation | 0.048 | 0.048 | 0.000 |
| no_crisis | suicidal_ideation | 0.010 | 0.010 | 0.000 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 96.12%
	* 🧠 Cohen's Kappa: 0.94
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               24 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                2 |          97 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          20 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  2 |
| suicidal_ideation             |                1 |           0 |                        0 |           0 |                               0 |                  36 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |    0.06     |                        0 |    0        |                               0 |            0.027027 |                  0 |  0 |
| no_crisis                     |         0.06     |    0        |                        0 |    0.047619 |                               0 |            0.01     |                  0 |  0 |
| risk_taking_behaviours        |         0        |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| self-harm                     |         0        |    0.047619 |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| substance_abuse_or_withdrawal |         0        |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| suicidal_ideation             |         0.027027 |    0.01     |                        0 |    0        |                               0 |            0        |                  0 |  0 |
| violent_thoughts              |         0        |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |
|                               |         0        |    0        |                        0 |    0        |                               0 |            0        |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.040 | 25 |
| no_crisis | anxiety_crisis | 0.020 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.048 | 21 |
| substance_abuse_or_withdrawal |  | 0.111 | 18 |
| suicidal_ideation | anxiety_crisis | 0.027 | 37 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.060 | 0.040 | 0.020 |
| no_crisis | self-harm | 0.048 | 0.000 | 0.048 |
| anxiety_crisis | suicidal_ideation | 0.027 | 0.000 | 0.027 |
| no_crisis | suicidal_ideation | 0.010 | 0.010 | 0.000 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 89.81%
	* 🧠 Cohen's Kappa: 0.85
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               19 |           6 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                5 |          93 |                        0 |           0 |                               0 |                   1 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          17 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  36 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.29      |                        0 |   0         |                       0.0555556 |           0         |                0   |  0 |
| no_crisis                     |        0.29      |   0         |                        0 |   0.0952381 |                       0.0555556 |           0.037027  |                0   |  0 |
| risk_taking_behaviours        |        0         |   0         |                        0 |   0         |                       0         |           0         |                0   |  0 |
| self-harm                     |        0         |   0.0952381 |                        0 |   0         |                       0         |           0.0952381 |                0   |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |   0.0555556 |                        0 |   0         |                       0         |           0         |                0   |  0 |
| suicidal_ideation             |        0         |   0.037027  |                        0 |   0.0952381 |                       0         |           0         |                0.2 |  0 |
| violent_thoughts              |        0         |   0         |                        0 |   0         |                       0         |           0.2       |                0   |  0 |
|                               |        0         |   0         |                        0 |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.240 | 25 |
| no_crisis | anxiety_crisis | 0.050 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.095 | 21 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | no_crisis | 0.027 | 37 |
| violent_thoughts | suicidal_ideation | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.290 | 0.240 | 0.050 |
| suicidal_ideation | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | self-harm | 0.095 | 0.000 | 0.095 |
| self-harm | suicidal_ideation | 0.095 | 0.095 | 0.000 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 87.86%
	* 🧠 Cohen's Kappa: 0.82
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |          10 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                1 |          94 |                        1 |           0 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          17 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  35 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.41      |                     0    |   0         |                       0.0555556 |           0         |               0    |  0 |
| no_crisis                     |        0.41      |   0         |                     0.01 |   0.0952381 |                       0.0655556 |           0.0740541 |               0.01 |  0 |
| risk_taking_behaviours        |        0         |   0.01      |                     0    |   0         |                       0         |           0         |               0.2  |  0 |
| self-harm                     |        0         |   0.0952381 |                     0    |   0         |                       0         |           0.0952381 |               0    |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |   0.0655556 |                     0    |   0         |                       0         |           0         |               0    |  0 |
| suicidal_ideation             |        0         |   0.0740541 |                     0    |   0.0952381 |                       0         |           0         |               0    |  0 |
| violent_thoughts              |        0         |   0.01      |                     0.2  |   0         |                       0         |           0         |               0    |  0 |
|                               |        0         |   0         |                     0    |   0         |                       0         |           0         |               0    |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.400 | 25 |
| no_crisis | suicidal_ideation | 0.020 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.095 | 21 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | no_crisis | 0.054 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.410 | 0.400 | 0.010 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | self-harm | 0.095 | 0.000 | 0.095 |
| self-harm | suicidal_ideation | 0.095 | 0.095 | 0.000 |
| no_crisis | suicidal_ideation | 0.074 | 0.020 | 0.054 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 89.81%
	* 🧠 Cohen's Kappa: 0.85
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               14 |          11 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                0 |          98 |                        0 |           0 |                               1 |                   0 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          17 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  35 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.44      |                 0        |   0         |                       0.0555556 |           0         |               0    |  0 |
| no_crisis                     |        0.44      |   0         |                 0        |   0.047619  |                       0.0655556 |           0.0540541 |               0.01 |  0 |
| risk_taking_behaviours        |        0         |   0         |                 0        |   0.047619  |                       0         |           0         |               0    |  0 |
| self-harm                     |        0         |   0.047619  |                 0.047619 |   0         |                       0         |           0.0952381 |               0    |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |   0.0655556 |                 0        |   0         |                       0         |           0         |               0    |  0 |
| suicidal_ideation             |        0         |   0.0540541 |                 0        |   0.0952381 |                       0         |           0         |               0    |  0 |
| violent_thoughts              |        0         |   0.01      |                 0        |   0         |                       0         |           0         |               0    |  0 |
|                               |        0         |   0         |                 0        |   0         |                       0         |           0         |               0    |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.440 | 25 |
| no_crisis | substance_abuse_or_withdrawal | 0.010 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.095 | 21 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | no_crisis | 0.054 | 37 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.440 | 0.440 | 0.000 |
| self-harm | suicidal_ideation | 0.095 | 0.095 | 0.000 |
| no_crisis | substance_abuse_or_withdrawal | 0.066 | 0.010 | 0.056 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |
| no_crisis | suicidal_ideation | 0.054 | 0.000 | 0.054 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 83.98%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                8 |          80 |                        0 |           0 |                               1 |                   7 |                  1 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          14 |                               1 |                   3 |                  0 |  1 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              17 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  33 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.08     |                 0        |    0        |                       0.0555556 |            0        |               0    |  0 |
| no_crisis                     |        0.08      |    0        |                 0        |    0.047619 |                       0.01      |            0.097027 |               0.01 |  0 |
| risk_taking_behaviours        |        0         |    0        |                 0        |    0.047619 |                       0         |            0        |               0.2  |  0 |
| self-harm                     |        0         |    0.047619 |                 0.047619 |    0        |                       0.047619  |            0.142857 |               0    |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |    0.01     |                 0        |    0.047619 |                       0         |            0        |               0    |  0 |
| suicidal_ideation             |        0         |    0.097027 |                 0        |    0.142857 |                       0         |            0        |               0    |  0 |
| violent_thoughts              |        0         |    0.01     |                 0.2      |    0        |                       0         |            0        |               0    |  0 |
|                               |        0         |    0        |                 0        |    0        |                       0         |            0        |               0    |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 25 |
| no_crisis | anxiety_crisis | 0.080 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.143 | 21 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation |  | 0.081 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.143 | 0.143 | 0.000 |
| no_crisis | suicidal_ideation | 0.097 | 0.070 | 0.027 |
| anxiety_crisis | no_crisis | 0.080 | 0.000 | 0.080 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 84.47%
	* 🧠 Cohen's Kappa: 0.79
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                9 |          79 |                        0 |           0 |                               0 |                   7 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          14 |                               1 |                   5 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  34 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |             0    |    0.09     |                 0        |    0        |                        0        |            0        |               0    |  0 |
| no_crisis                     |             0.09 |    0        |                 0        |    0        |                        0        |            0.097027 |               0.01 |  0 |
| risk_taking_behaviours        |             0    |    0        |                 0        |    0.047619 |                        0        |            0        |               0.2  |  0 |
| self-harm                     |             0    |    0        |                 0.047619 |    0        |                        0.047619 |            0.238095 |               0    |  0 |
| substance_abuse_or_withdrawal |             0    |    0        |                 0        |    0.047619 |                        0        |            0        |               0    |  0 |
| suicidal_ideation             |             0    |    0.097027 |                 0        |    0.238095 |                        0        |            0        |               0    |  0 |
| violent_thoughts              |             0    |    0.01     |                 0.2      |    0        |                        0        |            0        |               0    |  0 |
|                               |             0    |    0        |                 0        |    0        |                        0        |            0        |               0    |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 25 |
| no_crisis | anxiety_crisis | 0.090 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.238 | 21 |
| substance_abuse_or_withdrawal | n/a | n/a | 18 |
| suicidal_ideation |  | 0.054 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| self-harm | suicidal_ideation | 0.238 | 0.238 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.097 | 0.070 | 0.027 |
| anxiety_crisis | no_crisis | 0.090 | 0.000 | 0.090 |
| risk_taking_behaviours | self-harm | 0.048 | 0.000 | 0.048 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 83.98%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                7 |          82 |                        0 |           0 |                               0 |                   5 |                  1 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          14 |                               1 |                   4 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              17 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  31 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.07     |                 0        |    0        |                       0.0555556 |            0        |               0    |  0 |
| no_crisis                     |        0.07      |    0        |                 0        |    0.047619 |                       0         |            0.077027 |               0.01 |  0 |
| risk_taking_behaviours        |        0         |    0        |                 0        |    0.047619 |                       0         |            0        |               0.2  |  0 |
| self-harm                     |        0         |    0.047619 |                 0.047619 |    0        |                       0.047619  |            0.190476 |               0    |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |    0        |                 0        |    0.047619 |                       0         |            0        |               0    |  0 |
| suicidal_ideation             |        0         |    0.077027 |                 0        |    0.190476 |                       0         |            0        |               0    |  0 |
| violent_thoughts              |        0         |    0.01     |                 0.2      |    0        |                       0         |            0        |               0    |  0 |
|                               |        0         |    0        |                 0        |    0        |                       0         |            0        |               0    |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 25 |
| no_crisis | anxiety_crisis | 0.070 | 100 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.190 | 21 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation |  | 0.135 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.190 | 0.190 | 0.000 |
| no_crisis | suicidal_ideation | 0.077 | 0.050 | 0.027 |
| anxiety_crisis | no_crisis | 0.070 | 0.000 | 0.070 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json`:
	* 🟩 Agreement Rate: 95.15%
	* 🧠 Cohen's Kappa: 0.93
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               23 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                3 |          97 |                        0 |           1 |                               0 |                   0 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          18 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  2 |
| suicidal_ideation             |                1 |           0 |                        0 |           1 |                               0 |                  37 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.029703  |                        0 |   0         |                               0 |            0.025641 |                  0 |  0 |
| no_crisis                     |         0.029703 |   0         |                        0 |   0.0625326 |                               0 |            0        |                  0 |  0 |
| risk_taking_behaviours        |         0        |   0         |                        0 |   0         |                               0 |            0        |                  0 |  0 |
| self-harm                     |         0        |   0.0625326 |                        0 |   0         |                               0 |            0.025641 |                  0 |  0 |
| substance_abuse_or_withdrawal |         0        |   0         |                        0 |   0         |                               0 |            0        |                  0 |  0 |
| suicidal_ideation             |         0.025641 |   0         |                        0 |   0.025641  |                               0 |            0        |                  0 |  0 |
| violent_thoughts              |         0        |   0         |                        0 |   0         |                               0 |            0        |                  0 |  0 |
|                               |         0        |   0         |                        0 |   0         |                               0 |            0        |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 23 |
| no_crisis | anxiety_crisis | 0.030 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.053 | 19 |
| substance_abuse_or_withdrawal |  | 0.111 | 18 |
| suicidal_ideation | anxiety_crisis | 0.026 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | self-harm | 0.063 | 0.010 | 0.053 |
| anxiety_crisis | no_crisis | 0.030 | 0.000 | 0.030 |
| anxiety_crisis | suicidal_ideation | 0.026 | 0.000 | 0.026 |
| self-harm | suicidal_ideation | 0.026 | 0.000 | 0.026 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 88.35%
	* 🧠 Cohen's Kappa: 0.83
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               17 |           6 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                6 |          92 |                        0 |           1 |                               0 |                   1 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          16 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  37 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.320276  |                        0 |   0         |                       0.0555556 |           0.025641  |                0   |  0 |
| no_crisis                     |        0.320276  |   0         |                        0 |   0.115164  |                       0.0555556 |           0.035542  |                0   |  0 |
| risk_taking_behaviours        |        0         |   0         |                        0 |   0         |                       0         |           0         |                0   |  0 |
| self-harm                     |        0         |   0.115164  |                        0 |   0         |                       0         |           0.0526316 |                0   |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |   0.0555556 |                        0 |   0         |                       0         |           0         |                0   |  0 |
| suicidal_ideation             |        0.025641  |   0.035542  |                        0 |   0.0526316 |                       0         |           0         |                0.2 |  0 |
| violent_thoughts              |        0         |   0         |                        0 |   0         |                       0         |           0.2       |                0   |  0 |
|                               |        0         |   0         |                        0 |   0         |                       0         |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.261 | 23 |
| no_crisis | anxiety_crisis | 0.059 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.105 | 19 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | anxiety_crisis | 0.026 | 39 |
| violent_thoughts | suicidal_ideation | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.320 | 0.261 | 0.059 |
| suicidal_ideation | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | self-harm | 0.115 | 0.010 | 0.105 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |
| no_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 86.89%
	* 🧠 Cohen's Kappa: 0.81
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               14 |           9 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                2 |          93 |                        1 |           1 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           2 |                        0 |          16 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           3 |                        0 |           0 |                               0 |                  36 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.411106   |               0          |   0         |                       0.0555556 |           0         |         0          |  0 |
| no_crisis                     |        0.411106  |  0          |               0.00990099 |   0.115164  |                       0.0654565 |           0.0967251 |         0.00990099 |  0 |
| risk_taking_behaviours        |        0         |  0.00990099 |               0          |   0         |                       0         |           0         |         0.2        |  0 |
| self-harm                     |        0         |  0.115164   |               0          |   0         |                       0         |           0.0526316 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |  0.0654565  |               0          |   0         |                       0         |           0         |         0          |  0 |
| suicidal_ideation             |        0         |  0.0967251  |               0          |   0.0526316 |                       0         |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00990099 |               0.2        |   0         |                       0         |           0         |         0          |  0 |
|                               |        0         |  0          |               0          |   0         |                       0         |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.391 | 23 |
| no_crisis | anxiety_crisis | 0.020 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.105 | 19 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | no_crisis | 0.077 | 39 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.411 | 0.391 | 0.020 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | self-harm | 0.115 | 0.010 | 0.105 |
| no_crisis | suicidal_ideation | 0.097 | 0.020 | 0.077 |
| no_crisis | substance_abuse_or_withdrawal | 0.065 | 0.010 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 89.32%
	* 🧠 Cohen's Kappa: 0.84
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               13 |          10 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                1 |          97 |                        1 |           0 |                               1 |                   0 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          17 |                               0 |                   1 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           3 |                        0 |           0 |                               0 |                  36 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.444684   |               0          |   0         |                       0.0555556 |           0         |         0          |  0 |
| no_crisis                     |        0.444684  |  0          |               0.00990099 |   0.0526316 |                       0.0654565 |           0.0769231 |         0.00990099 |  0 |
| risk_taking_behaviours        |        0         |  0.00990099 |               0          |   0         |                       0         |           0         |         0          |  0 |
| self-harm                     |        0         |  0.0526316  |               0          |   0         |                       0         |           0.0526316 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |  0.0654565  |               0          |   0         |                       0         |           0         |         0          |  0 |
| suicidal_ideation             |        0         |  0.0769231  |               0          |   0.0526316 |                       0         |           0         |         0          |  0 |
| violent_thoughts              |        0         |  0.00990099 |               0          |   0         |                       0         |           0         |         0          |  0 |
|                               |        0         |  0          |               0          |   0         |                       0         |           0         |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.435 | 23 |
| no_crisis | anxiety_crisis | 0.010 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | no_crisis | 0.053 | 19 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation | no_crisis | 0.077 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.445 | 0.435 | 0.010 |
| no_crisis | suicidal_ideation | 0.077 | 0.000 | 0.077 |
| no_crisis | substance_abuse_or_withdrawal | 0.065 | 0.010 | 0.056 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |
| no_crisis | self-harm | 0.053 | 0.000 | 0.053 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 83.50%
	* 🧠 Cohen's Kappa: 0.77
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               23 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               10 |          79 |                        0 |           0 |                               1 |                   6 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          14 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              17 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  35 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.0990099  |                0         |   0         |                      0.0555556  |            0        |         0          |  0 |
| no_crisis                     |        0.0990099 |  0          |                0         |   0.0526316 |                      0.00990099 |            0.085047 |         0.00990099 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0526316 |                      0          |            0        |         0.2        |  0 |
| self-harm                     |        0         |  0.0526316  |                0.0526316 |   0         |                      0.0526316  |            0.105263 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |  0.00990099 |                0         |   0.0526316 |                      0          |            0        |         0          |  0 |
| suicidal_ideation             |        0         |  0.085047   |                0         |   0.105263  |                      0          |            0        |         0          |  0 |
| violent_thoughts              |        0         |  0.00990099 |                0.2       |   0         |                      0          |            0        |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                      0          |            0        |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 23 |
| no_crisis | anxiety_crisis | 0.099 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.105 | 19 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation |  | 0.077 | 39 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.105 | 0.105 | 0.000 |
| anxiety_crisis | no_crisis | 0.099 | 0.000 | 0.099 |
| no_crisis | suicidal_ideation | 0.085 | 0.059 | 0.026 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 83.98%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               23 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               11 |          78 |                        0 |           0 |                               0 |                   7 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          14 |                               1 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  36 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.108911   |                0         |   0         |                       0         |            0        |         0          |  0 |
| no_crisis                     |         0.108911 |  0          |                0         |   0         |                       0         |            0.094948 |         0.00990099 |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |   0.0526316 |                       0         |            0        |         0.2        |  0 |
| self-harm                     |         0        |  0          |                0.0526316 |   0         |                       0.0526316 |            0.157895 |         0          |  0 |
| substance_abuse_or_withdrawal |         0        |  0          |                0         |   0.0526316 |                       0         |            0        |         0          |  0 |
| suicidal_ideation             |         0        |  0.094948   |                0         |   0.157895  |                       0         |            0        |         0          |  0 |
| violent_thoughts              |         0        |  0.00990099 |                0.2       |   0         |                       0         |            0        |         0          |  0 |
|                               |         0        |  0          |                0         |   0         |                       0         |            0        |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 23 |
| no_crisis | anxiety_crisis | 0.109 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.158 | 19 |
| substance_abuse_or_withdrawal | n/a | n/a | 18 |
| suicidal_ideation |  | 0.051 | 39 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.158 | 0.158 | 0.000 |
| anxiety_crisis | no_crisis | 0.109 | 0.000 | 0.109 |
| no_crisis | suicidal_ideation | 0.095 | 0.069 | 0.026 |
| risk_taking_behaviours | self-harm | 0.053 | 0.000 | 0.053 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 82.52%
	* 🧠 Cohen's Kappa: 0.76
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               23 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                9 |          80 |                        0 |           0 |                               0 |                   6 |                  1 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          14 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              17 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  32 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.0891089  |                0         |   0         |                       0.0555556 |            0        |         0          |  0 |
| no_crisis                     |        0.0891089 |  0          |                0         |   0.0526316 |                       0         |            0.110688 |         0.00990099 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0526316 |                       0         |            0        |         0.2        |  0 |
| self-harm                     |        0         |  0.0526316  |                0.0526316 |   0         |                       0.0526316 |            0.105263 |         0          |  0 |
| substance_abuse_or_withdrawal |        0.0555556 |  0          |                0         |   0.0526316 |                       0         |            0        |         0          |  0 |
| suicidal_ideation             |        0         |  0.110688   |                0         |   0.105263  |                       0         |            0        |         0          |  0 |
| violent_thoughts              |        0         |  0.00990099 |                0.2       |   0         |                       0         |            0        |         0          |  0 |
|                               |        0         |  0          |                0         |   0         |                       0         |            0        |         0          |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 23 |
| no_crisis | anxiety_crisis | 0.089 | 101 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.105 | 19 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.056 | 18 |
| suicidal_ideation |  | 0.128 | 39 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.111 | 0.059 | 0.051 |
| self-harm | suicidal_ideation | 0.105 | 0.105 | 0.000 |
| anxiety_crisis | no_crisis | 0.089 | 0.000 | 0.089 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.056 | 0.000 | 0.056 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json`:
	* 🟩 Agreement Rate: 88.35%
	* 🧠 Cohen's Kappa: 0.83
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               19 |           7 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                4 |          93 |                        0 |           0 |                               0 |                   1 |                  0 |  1 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          17 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              14 |                   0 |                  0 |  0 |
| suicidal_ideation             |                1 |           1 |                        0 |           0 |                               0 |                  35 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |    0.299663 |                        0 |        0    |                          0.0625 |           0.0640641 |                0   |  0 |
| no_crisis                     |        0.299663  |    0        |                        0 |        0.05 |                          0.0625 |           0.037128  |                0   |  0 |
| risk_taking_behaviours        |        0         |    0        |                        0 |        0    |                          0      |           0         |                0   |  0 |
| self-harm                     |        0         |    0.05     |                        0 |        0    |                          0      |           0.1       |                0   |  0 |
| substance_abuse_or_withdrawal |        0.0625    |    0.0625   |                        0 |        0    |                          0      |           0         |                0   |  0 |
| suicidal_ideation             |        0.0640641 |    0.037128 |                        0 |        0.1  |                          0      |           0         |                0.2 |  0 |
| violent_thoughts              |        0         |    0        |                        0 |        0    |                          0      |           0.2       |                0   |  0 |
|                               |        0         |    0        |                        0 |        0    |                          0      |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.259 | 27 |
| no_crisis | anxiety_crisis | 0.040 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.100 | 20 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.062 | 16 |
| suicidal_ideation | anxiety_crisis | 0.027 | 37 |
| violent_thoughts | suicidal_ideation | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.300 | 0.259 | 0.040 |
| suicidal_ideation | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.100 | 0.100 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.064 | 0.037 | 0.027 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.062 | 0.000 | 0.062 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 87.38%
	* 🧠 Cohen's Kappa: 0.82
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |          11 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                0 |          94 |                        1 |           0 |                               1 |                   2 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        0 |          17 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              14 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  35 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.407407  |                 0        |        0    |                        0.0625   |           0         |           0        |  0 |
| no_crisis                     |         0.407407 |   0         |                 0.010101 |        0.05 |                        0.072601 |           0.0742561 |           0.010101 |  0 |
| risk_taking_behaviours        |         0        |   0.010101  |                 0        |        0    |                        0        |           0         |           0.2      |  0 |
| self-harm                     |         0        |   0.05      |                 0        |        0    |                        0        |           0.1       |           0        |  0 |
| substance_abuse_or_withdrawal |         0.0625   |   0.072601  |                 0        |        0    |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |         0        |   0.0742561 |                 0        |        0.1  |                        0        |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.010101  |                 0.2      |        0    |                        0        |           0         |           0        |  0 |
|                               |         0        |   0         |                 0        |        0    |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.407 | 27 |
| no_crisis | suicidal_ideation | 0.020 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.100 | 20 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.062 | 16 |
| suicidal_ideation | no_crisis | 0.054 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.407 | 0.407 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.100 | 0.100 | 0.000 |
| no_crisis | suicidal_ideation | 0.074 | 0.020 | 0.054 |
| no_crisis | substance_abuse_or_withdrawal | 0.073 | 0.010 | 0.062 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 87.38%
	* 🧠 Cohen's Kappa: 0.81
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               14 |          13 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                0 |          96 |                        0 |           1 |                               1 |                   0 |                  1 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          16 |                               0 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           1 |                        0 |           0 |                              14 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  35 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.481481  |                     0    |    0        |                        0.0625   |           0         |           0        |  0 |
| no_crisis                     |         0.481481 |   0         |                     0    |    0.060101 |                        0.072601 |           0.0540541 |           0.010101 |  0 |
| risk_taking_behaviours        |         0        |   0         |                     0    |    0.05     |                        0        |           0         |           0        |  0 |
| self-harm                     |         0        |   0.060101  |                     0.05 |    0        |                        0        |           0.1       |           0        |  0 |
| substance_abuse_or_withdrawal |         0.0625   |   0.072601  |                     0    |    0        |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |         0        |   0.0540541 |                     0    |    0.1      |                        0        |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.010101  |                     0    |    0        |                        0        |           0         |           0        |  0 |
|                               |         0        |   0         |                     0    |    0        |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.481 | 27 |
| no_crisis | self-harm | 0.010 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.100 | 20 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.062 | 16 |
| suicidal_ideation | no_crisis | 0.054 | 37 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.481 | 0.481 | 0.000 |
| self-harm | suicidal_ideation | 0.100 | 0.100 | 0.000 |
| no_crisis | substance_abuse_or_withdrawal | 0.073 | 0.010 | 0.062 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.062 | 0.000 | 0.062 |
| no_crisis | self-harm | 0.060 | 0.010 | 0.050 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 82.04%
	* 🧠 Cohen's Kappa: 0.76
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |           1 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                8 |          79 |                        0 |           1 |                               1 |                   6 |                  1 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          13 |                               1 |                   3 |                  0 |  1 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  33 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.117845  |                     0    |    0        |                        0.0625   |           0.037037  |           0        |  0 |
| no_crisis                     |         0.117845 |   0         |                     0    |    0.060101 |                        0.010101 |           0.0876331 |           0.010101 |  0 |
| risk_taking_behaviours        |         0        |   0         |                     0    |    0.05     |                        0        |           0         |           0.2      |  0 |
| self-harm                     |         0        |   0.060101  |                     0.05 |    0        |                        0.05     |           0.15      |           0        |  0 |
| substance_abuse_or_withdrawal |         0.0625   |   0.010101  |                     0    |    0.05     |                        0        |           0         |           0        |  0 |
| suicidal_ideation             |         0.037037 |   0.0876331 |                     0    |    0.15     |                        0        |           0         |           0        |  0 |
| violent_thoughts              |         0        |   0.010101  |                     0.2  |    0        |                        0        |           0         |           0        |  0 |
|                               |         0        |   0         |                     0    |    0        |                        0        |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.037 | 27 |
| no_crisis | anxiety_crisis | 0.081 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.150 | 20 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.062 | 16 |
| suicidal_ideation |  | 0.081 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.150 | 0.150 | 0.000 |
| anxiety_crisis | no_crisis | 0.118 | 0.037 | 0.081 |
| no_crisis | suicidal_ideation | 0.088 | 0.061 | 0.027 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.062 | 0.000 | 0.062 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 83.50%
	* 🧠 Cohen's Kappa: 0.78
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               26 |           0 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                8 |          79 |                        0 |           1 |                               0 |                   6 |                  1 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          13 |                               1 |                   5 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  34 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.0808081 |                     0    |    0        |                            0    |           0.037037  |           0        |  0 |
| no_crisis                     |        0.0808081 |   0         |                     0    |    0.010101 |                            0    |           0.0876331 |           0.010101 |  0 |
| risk_taking_behaviours        |        0         |   0         |                     0    |    0.05     |                            0    |           0         |           0.2      |  0 |
| self-harm                     |        0         |   0.010101  |                     0.05 |    0        |                            0.05 |           0.25      |           0        |  0 |
| substance_abuse_or_withdrawal |        0         |   0         |                     0    |    0.05     |                            0    |           0         |           0        |  0 |
| suicidal_ideation             |        0.037037  |   0.0876331 |                     0    |    0.25     |                            0    |           0         |           0        |  0 |
| violent_thoughts              |        0         |   0.010101  |                     0.2  |    0        |                            0    |           0         |           0        |  0 |
|                               |        0         |   0         |                     0    |    0        |                            0    |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | suicidal_ideation | 0.037 | 27 |
| no_crisis | anxiety_crisis | 0.081 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.250 | 20 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.054 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| self-harm | suicidal_ideation | 0.250 | 0.250 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| no_crisis | suicidal_ideation | 0.088 | 0.061 | 0.027 |
| anxiety_crisis | no_crisis | 0.081 | 0.000 | 0.081 |
| risk_taking_behaviours | self-harm | 0.050 | 0.000 | 0.050 |

### `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 81.07%
	* 🧠 Cohen's Kappa: 0.74
Confusion Matrix between `gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               25 |           1 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                7 |          80 |                        0 |           1 |                               0 |                   5 |                  1 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           1 |                        1 |          13 |                               1 |                   4 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              15 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  30 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               2 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |    0.107744 |                     0    |    0        |                          0.0625 |            0.037037 |           0        |  0 |
| no_crisis                     |         0.107744 |    0        |                     0    |    0.060101 |                          0      |            0.104559 |           0.010101 |  0 |
| risk_taking_behaviours        |         0        |    0        |                     0    |    0.05     |                          0      |            0        |           0.2      |  0 |
| self-harm                     |         0        |    0.060101 |                     0.05 |    0        |                          0.05   |            0.2      |           0        |  0 |
| substance_abuse_or_withdrawal |         0.0625   |    0        |                     0    |    0.05     |                          0      |            0        |           0        |  0 |
| suicidal_ideation             |         0.037037 |    0.104559 |                     0    |    0.2      |                          0      |            0        |           0        |  0 |
| violent_thoughts              |         0        |    0.010101 |                     0.2  |    0        |                          0      |            0        |           0        |  0 |
|                               |         0        |    0        |                     0    |    0        |                          0      |            0        |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.037 | 27 |
| no_crisis | anxiety_crisis | 0.071 | 99 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.200 | 20 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.062 | 16 |
| suicidal_ideation |  | 0.135 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.200 | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.200 | 0.000 | 0.200 |
| self-harm | suicidal_ideation | 0.200 | 0.200 | 0.000 |
| anxiety_crisis | no_crisis | 0.108 | 0.037 | 0.071 |
| no_crisis | suicidal_ideation | 0.105 | 0.051 | 0.054 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.062 | 0.000 | 0.062 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json`:
	* 🟩 Agreement Rate: 91.26%
	* 🧠 Cohen's Kappa: 0.87
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |           9 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |                2 |          99 |                        1 |           0 |                               1 |                   0 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          17 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  38 |                  1 |  0 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.379417   |               0          |           0 |                      0          |               0.04  |              0     |  0 |
| no_crisis                     |         0.379417 |  0          |               0.00970874 |           0 |                      0.00970874 |               0.025 |              0     |  0 |
| risk_taking_behaviours        |         0        |  0.00970874 |               0          |           0 |                      0          |               0     |              0.25  |  0 |
| self-harm                     |         0        |  0          |               0          |           0 |                      0          |               0     |              0     |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00970874 |               0          |           0 |                      0          |               0     |              0     |  0 |
| suicidal_ideation             |         0.04     |  0.025      |               0          |           0 |                      0          |               0     |              0.025 |  0 |
| violent_thoughts              |         0        |  0          |               0.25       |           0 |                      0          |               0.025 |              0     |  0 |
|                               |         0        |  0          |               0          |           0 |                      0          |               0     |              0     |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.360 | 25 |
| no_crisis | anxiety_crisis | 0.019 | 103 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | n/a | n/a | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation | no_crisis | 0.025 | 40 |
| violent_thoughts | risk_taking_behaviours | 0.250 | 4 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.379 | 0.360 | 0.019 |
| risk_taking_behaviours | violent_thoughts | 0.250 | 0.000 | 0.250 |
| anxiety_crisis | suicidal_ideation | 0.040 | 0.040 | 0.000 |
| no_crisis | suicidal_ideation | 0.025 | 0.000 | 0.025 |
| suicidal_ideation | violent_thoughts | 0.025 | 0.025 | 0.000 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 89.81%
	* 🧠 Cohen's Kappa: 0.85
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               13 |          12 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                2 |          99 |                        0 |           1 |                               1 |                   0 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          16 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  37 |                  1 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  4 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.499417   |                0         |  0          |                      0          |               0     |              0     |  0 |
| no_crisis                     |         0.499417 |  0          |                0         |  0.00970874 |                      0.00970874 |               0.05  |              0     |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |  0.0588235  |                      0          |               0     |              0     |  0 |
| self-harm                     |         0        |  0.00970874 |                0.0588235 |  0          |                      0          |               0     |              0     |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00970874 |                0         |  0          |                      0          |               0     |              0     |  0 |
| suicidal_ideation             |         0        |  0.05       |                0         |  0          |                      0          |               0     |              0.025 |  0 |
| violent_thoughts              |         0        |  0          |                0         |  0          |                      0          |               0.025 |              0     |  0 |
|                               |         0        |  0          |                0         |  0          |                      0          |               0     |              0     |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.480 | 25 |
| no_crisis | anxiety_crisis | 0.019 | 103 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | risk_taking_behaviours | 0.059 | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation | no_crisis | 0.050 | 40 |
| violent_thoughts | n/a | n/a | 4 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.499 | 0.480 | 0.019 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |
| no_crisis | suicidal_ideation | 0.050 | 0.000 | 0.050 |
| suicidal_ideation | violent_thoughts | 0.025 | 0.025 | 0.000 |
| no_crisis | self-harm | 0.010 | 0.010 | 0.000 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 79.61%
	* 🧠 Cohen's Kappa: 0.72
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           3 |                        0 |           0 |                               0 |                   2 |                  0 |  0 |
| no_crisis                     |               14 |          78 |                        0 |           2 |                               2 |                   4 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   2 |                  0 |  1 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  35 |                  1 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |   0.255922  |                0         |   0         |                       0         |            0.08     |              0     |  0 |
| no_crisis                     |         0.255922 |   0         |                0         |   0.0194175 |                       0.0194175 |            0.063835 |              0     |  0 |
| risk_taking_behaviours        |         0        |   0         |                0         |   0.0588235 |                       0         |            0        |              0.25  |  0 |
| self-harm                     |         0        |   0.0194175 |                0.0588235 |   0         |                       0.0588235 |            0.117647 |              0     |  0 |
| substance_abuse_or_withdrawal |         0        |   0.0194175 |                0         |   0.0588235 |                       0         |            0        |              0     |  0 |
| suicidal_ideation             |         0.08     |   0.063835  |                0         |   0.117647  |                       0         |            0        |              0.025 |  0 |
| violent_thoughts              |         0        |   0         |                0.25      |   0         |                       0         |            0.025    |              0     |  0 |
|                               |         0        |   0         |                0         |   0         |                       0         |            0        |              0     |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.120 | 25 |
| no_crisis | anxiety_crisis | 0.136 | 103 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.118 | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.075 | 40 |
| violent_thoughts | risk_taking_behaviours | 0.250 | 4 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.256 | 0.120 | 0.136 |
| risk_taking_behaviours | violent_thoughts | 0.250 | 0.000 | 0.250 |
| self-harm | suicidal_ideation | 0.118 | 0.118 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.080 | 0.080 | 0.000 |
| no_crisis | suicidal_ideation | 0.064 | 0.039 | 0.025 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 80.58%
	* 🧠 Cohen's Kappa: 0.73
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           2 |                        0 |           0 |                               1 |                   2 |                  0 |  0 |
| no_crisis                     |               14 |          78 |                        0 |           2 |                               1 |                   4 |                  0 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           0 |                        0 |           0 |                               0 |                  37 |                  1 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.215922   |                0         |   0         |                      0.04       |            0.08     |              0     |  0 |
| no_crisis                     |         0.215922 |  0          |                0         |   0.0194175 |                      0.00970874 |            0.038835 |              0     |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |   0.0588235 |                      0          |            0        |              0.25  |  0 |
| self-harm                     |         0        |  0.0194175  |                0.0588235 |   0         |                      0.0588235  |            0.176471 |              0     |  0 |
| substance_abuse_or_withdrawal |         0.04     |  0.00970874 |                0         |   0.0588235 |                      0          |            0        |              0     |  0 |
| suicidal_ideation             |         0.08     |  0.038835   |                0         |   0.176471  |                      0          |            0        |              0.025 |  0 |
| violent_thoughts              |         0        |  0          |                0.25      |   0         |                      0          |            0.025    |              0     |  0 |
|                               |         0        |  0          |                0         |   0         |                      0          |            0        |              0     |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.080 | 25 |
| no_crisis | anxiety_crisis | 0.136 | 103 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.176 | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.050 | 40 |
| violent_thoughts | risk_taking_behaviours | 0.250 | 4 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.250 | 0.000 | 0.250 |
| anxiety_crisis | no_crisis | 0.216 | 0.080 | 0.136 |
| self-harm | suicidal_ideation | 0.176 | 0.176 | 0.000 |
| anxiety_crisis | suicidal_ideation | 0.080 | 0.080 | 0.000 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 78.16%
	* 🧠 Cohen's Kappa: 0.70
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               20 |           4 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| no_crisis                     |               13 |          78 |                        0 |           2 |                               1 |                   4 |                  0 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  32 |                  1 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  3 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.286214   |                0         |   0         |                      0          |            0.04     |              0     |  0 |
| no_crisis                     |         0.286214 |  0          |                0         |   0.0194175 |                      0.00970874 |            0.088835 |              0     |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |   0.0588235 |                      0          |            0        |              0.25  |  0 |
| self-harm                     |         0        |  0.0194175  |                0.0588235 |   0         |                      0.0588235  |            0.176471 |              0     |  0 |
| substance_abuse_or_withdrawal |         0        |  0.00970874 |                0         |   0.0588235 |                      0          |            0        |              0     |  0 |
| suicidal_ideation             |         0.04     |  0.088835   |                0         |   0.176471  |                      0          |            0        |              0.025 |  0 |
| violent_thoughts              |         0        |  0          |                0.25      |   0         |                      0          |            0.025    |              0     |  0 |
|                               |         0        |  0          |                0         |   0         |                      0          |            0        |              0     |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.160 | 25 |
| no_crisis | anxiety_crisis | 0.126 | 103 |
| risk_taking_behaviours | n/a | n/a | 0 |
| self-harm | suicidal_ideation | 0.176 | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 16 |
| suicidal_ideation |  | 0.125 | 40 |
| violent_thoughts | risk_taking_behaviours | 0.250 | 4 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.286 | 0.160 | 0.126 |
| risk_taking_behaviours | violent_thoughts | 0.250 | 0.000 | 0.250 |
| self-harm | suicidal_ideation | 0.176 | 0.176 | 0.000 |
| no_crisis | suicidal_ideation | 0.089 | 0.039 | 0.050 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json`:
	* 🟩 Agreement Rate: 92.23%
	* 🧠 Cohen's Kappa: 0.88
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (ROWS) and `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               11 |           6 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                4 |         104 |                        0 |           1 |                               0 |                   0 |                  0 |  0 |
| risk_taking_behaviours        |                0 |           1 |                        0 |           0 |                               0 |                   0 |                  1 |  0 |
| self-harm                     |                0 |           0 |                        1 |          16 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           0 |                        0 |           0 |                              17 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  37 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.389638   |                0         |  0          |                               0 |           0         |                0   |  0 |
| no_crisis                     |         0.389638 |  0          |                0.5       |  0.00917431 |                               0 |           0.0512821 |                0   |  0 |
| risk_taking_behaviours        |         0        |  0.5        |                0         |  0.0588235  |                               0 |           0         |                0.5 |  0 |
| self-harm                     |         0        |  0.00917431 |                0.0588235 |  0          |                               0 |           0         |                0   |  0 |
| substance_abuse_or_withdrawal |         0        |  0          |                0         |  0          |                               0 |           0         |                0   |  0 |
| suicidal_ideation             |         0        |  0.0512821  |                0         |  0          |                               0 |           0         |                0   |  0 |
| violent_thoughts              |         0        |  0          |                0.5       |  0          |                               0 |           0         |                0   |  0 |
|                               |         0        |  0          |                0         |  0          |                               0 |           0         |                0   |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.353 | 17 |
| no_crisis | anxiety_crisis | 0.037 | 109 |
| risk_taking_behaviours | no_crisis | 0.500 | 2 |
| self-harm | risk_taking_behaviours | 0.059 | 17 |
| substance_abuse_or_withdrawal | n/a | n/a | 17 |
| suicidal_ideation | no_crisis | 0.051 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.500 | 0.000 | 0.500 |
| risk_taking_behaviours | violent_thoughts | 0.500 | 0.500 | 0.000 |
| anxiety_crisis | no_crisis | 0.390 | 0.353 | 0.037 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |
| no_crisis | suicidal_ideation | 0.051 | 0.000 | 0.051 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 80.10%
	* 🧠 Cohen's Kappa: 0.72
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               16 |          80 |                        0 |           2 |                               2 |                   6 |                  0 |  3 |
| risk_taking_behaviours        |                1 |           0 |                        1 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   2 |                  0 |  1 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  35 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.205613  |                0.5       |   0         |                       0.0588235 |           0         |                  0 |  0 |
| no_crisis                     |        0.205613  |   0         |                0         |   0.0183486 |                       0.0183486 |           0.0806869 |                  0 |  0 |
| risk_taking_behaviours        |        0.5       |   0         |                0         |   0.0588235 |                       0         |           0         |                  0 |  0 |
| self-harm                     |        0         |   0.0183486 |                0.0588235 |   0         |                       0.0588235 |           0.117647  |                  0 |  0 |
| substance_abuse_or_withdrawal |        0.0588235 |   0.0183486 |                0         |   0.0588235 |                       0         |           0         |                  0 |  0 |
| suicidal_ideation             |        0         |   0.0806869 |                0         |   0.117647  |                       0         |           0         |                  0 |  0 |
| violent_thoughts              |        0         |   0         |                0         |   0         |                       0         |           0         |                  0 |  0 |
|                               |        0         |   0         |                0         |   0         |                       0         |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.059 | 17 |
| no_crisis | anxiety_crisis | 0.147 | 109 |
| risk_taking_behaviours | anxiety_crisis | 0.500 | 2 |
| self-harm | suicidal_ideation | 0.118 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.077 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | risk_taking_behaviours | 0.500 | 0.000 | 0.500 |
| anxiety_crisis | no_crisis | 0.206 | 0.059 | 0.147 |
| self-harm | suicidal_ideation | 0.118 | 0.118 | 0.000 |
| no_crisis | suicidal_ideation | 0.081 | 0.055 | 0.026 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.059 | 0.000 | 0.059 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 81.07%
	* 🧠 Cohen's Kappa: 0.74
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |           0 |                        0 |           0 |                               1 |                   0 |                  0 |  0 |
| no_crisis                     |               17 |          80 |                        0 |           2 |                               1 |                   6 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  0 |  1 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           0 |                        0 |           0 |                               0 |                  37 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.155963   |                0         |   0         |                      0.117647   |           0         |                  0 |  0 |
| no_crisis                     |         0.155963 |  0          |                0         |   0.0183486 |                      0.00917431 |           0.0550459 |                  0 |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |   0.0588235 |                      0          |           0         |                  0 |  0 |
| self-harm                     |         0        |  0.0183486  |                0.0588235 |   0         |                      0.0588235  |           0.176471  |                  0 |  0 |
| substance_abuse_or_withdrawal |         0.117647 |  0.00917431 |                0         |   0.0588235 |                      0          |           0         |                  0 |  0 |
| suicidal_ideation             |         0        |  0.0550459  |                0         |   0.176471  |                      0          |           0         |                  0 |  0 |
| violent_thoughts              |         0        |  0          |                0         |   0         |                      0          |           0         |                  0 |  0 |
|                               |         0        |  0          |                0         |   0         |                      0          |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | substance_abuse_or_withdrawal | 0.059 | 17 |
| no_crisis | anxiety_crisis | 0.156 | 109 |
| risk_taking_behaviours |  | 0.500 | 2 |
| self-harm | suicidal_ideation | 0.176 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.051 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| self-harm | suicidal_ideation | 0.176 | 0.176 | 0.000 |
| anxiety_crisis | no_crisis | 0.156 | 0.000 | 0.156 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.118 | 0.059 | 0.059 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |
| self-harm | substance_abuse_or_withdrawal | 0.059 | 0.059 | 0.000 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 79.13%
	* 🧠 Cohen's Kappa: 0.71
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               16 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               16 |          81 |                        0 |           2 |                               1 |                   5 |                  0 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  0 |  1 |
| self-harm                     |                0 |           0 |                        1 |          12 |                               1 |                   3 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  32 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.205613   |                0         |   0         |                      0.0588235  |           0         |                  0 |  0 |
| no_crisis                     |        0.205613  |  0          |                0         |   0.0183486 |                      0.00917431 |           0.0971536 |                  0 |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |   0.0588235 |                      0          |           0         |                  0 |  0 |
| self-harm                     |        0         |  0.0183486  |                0.0588235 |   0         |                      0.0588235  |           0.176471  |                  0 |  0 |
| substance_abuse_or_withdrawal |        0.0588235 |  0.00917431 |                0         |   0.0588235 |                      0          |           0         |                  0 |  0 |
| suicidal_ideation             |        0         |  0.0971536  |                0         |   0.176471  |                      0          |           0         |                  0 |  0 |
| violent_thoughts              |        0         |  0          |                0         |   0         |                      0          |           0         |                  0 |  0 |
|                               |        0         |  0          |                0         |   0         |                      0          |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.059 | 17 |
| no_crisis | anxiety_crisis | 0.147 | 109 |
| risk_taking_behaviours |  | 0.500 | 2 |
| self-harm | suicidal_ideation | 0.176 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.128 | 39 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.206 | 0.059 | 0.147 |
| self-harm | suicidal_ideation | 0.176 | 0.176 | 0.000 |
| no_crisis | suicidal_ideation | 0.097 | 0.046 | 0.051 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.059 | 0.000 | 0.059 |
| risk_taking_behaviours | self-harm | 0.059 | 0.000 | 0.059 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json`:
	* 🟩 Agreement Rate: 79.13%
	* 🧠 Cohen's Kappa: 0.71
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               18 |          81 |                        0 |           1 |                               2 |                   8 |                  0 |  3 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  1 |
| self-harm                     |                0 |           0 |                        1 |          13 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  33 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.159292   |                0         |  0          |                       0.0588235 |           0         |           0        |  0 |
| no_crisis                     |        0.159292  |  0          |                0         |  0.00884956 |                       0.0176991 |           0.0978235 |           0        |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |  0.0588235  |                       0         |           0         |           0.166667 |  0 |
| self-harm                     |        0         |  0.00884956 |                0.0588235 |  0          |                       0.0588235 |           0.117647  |           0        |  0 |
| substance_abuse_or_withdrawal |        0.0588235 |  0.0176991  |                0         |  0.0588235  |                       0         |           0         |           0        |  0 |
| suicidal_ideation             |        0         |  0.0978235  |                0         |  0.117647   |                       0         |           0         |           0        |  0 |
| violent_thoughts              |        0         |  0          |                0.166667  |  0          |                       0         |           0         |           0        |  0 |
|                               |        0         |  0          |                0         |  0          |                       0         |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 15 |
| no_crisis | anxiety_crisis | 0.159 | 113 |
| risk_taking_behaviours |  | 1.000 | 1 |
| self-harm | suicidal_ideation | 0.118 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.081 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |
| anxiety_crisis | no_crisis | 0.159 | 0.000 | 0.159 |
| self-harm | suicidal_ideation | 0.118 | 0.118 | 0.000 |
| no_crisis | suicidal_ideation | 0.098 | 0.071 | 0.027 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.059 | 0.000 | 0.059 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 79.13%
	* 🧠 Cohen's Kappa: 0.71
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               14 |           0 |                        0 |           0 |                               1 |                   0 |                  0 |  0 |
| no_crisis                     |               19 |          80 |                        0 |           1 |                               1 |                   8 |                  0 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          13 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           0 |                        0 |           0 |                               0 |                  35 |                  0 |  2 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |         0        |  0.168142   |                0         |  0          |                      0.12549    |           0         |           0        |  0 |
| no_crisis                     |         0.168142 |  0          |                0         |  0.00884956 |                      0.00884956 |           0.0707965 |           0        |  0 |
| risk_taking_behaviours        |         0        |  0          |                0         |  0.0588235  |                      0          |           1         |           0.166667 |  0 |
| self-harm                     |         0        |  0.00884956 |                0.0588235 |  0          |                      0.0588235  |           0.117647  |           0        |  0 |
| substance_abuse_or_withdrawal |         0.12549  |  0.00884956 |                0         |  0.0588235  |                      0          |           0         |           0        |  0 |
| suicidal_ideation             |         0        |  0.0707965  |                1         |  0.117647   |                      0          |           0         |           0        |  0 |
| violent_thoughts              |         0        |  0          |                0.166667  |  0          |                      0          |           0         |           0        |  0 |
|                               |         0        |  0          |                0         |  0          |                      0          |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | substance_abuse_or_withdrawal | 0.067 | 15 |
| no_crisis | anxiety_crisis | 0.168 | 113 |
| risk_taking_behaviours | suicidal_ideation | 1.000 | 1 |
| self-harm | suicidal_ideation | 0.118 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.054 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | suicidal_ideation | 1.000 | 1.000 | 0.000 |
| anxiety_crisis | no_crisis | 0.168 | 0.000 | 0.168 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.125 | 0.067 | 0.059 |
| self-harm | suicidal_ideation | 0.118 | 0.118 | 0.000 |

### `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 79.13%
	* 🧠 Cohen's Kappa: 0.71
Confusion Matrix between `gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               15 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |               17 |          83 |                        0 |           1 |                               1 |                   6 |                  0 |  5 |
| risk_taking_behaviours        |                0 |           0 |                        0 |           0 |                               0 |                   1 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        1 |          13 |                               1 |                   2 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              16 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           1 |                        0 |           0 |                               0 |                  31 |                  0 |  5 |
| violent_thoughts              |                0 |           0 |                        1 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |  0.150442   |                0         |  0          |                      0.0588235  |           0         |           0        |  0 |
| no_crisis                     |        0.150442  |  0          |                0         |  0.00884956 |                      0.00884956 |           0.0801244 |           0        |  0 |
| risk_taking_behaviours        |        0         |  0          |                0         |  0.0588235  |                      0          |           1         |           0.166667 |  0 |
| self-harm                     |        0         |  0.00884956 |                0.0588235 |  0          |                      0.0588235  |           0.117647  |           0        |  0 |
| substance_abuse_or_withdrawal |        0.0588235 |  0.00884956 |                0         |  0.0588235  |                      0          |           0         |           0        |  0 |
| suicidal_ideation             |        0         |  0.0801244  |                1         |  0.117647   |                      0          |           0         |           0        |  0 |
| violent_thoughts              |        0         |  0          |                0.166667  |  0          |                      0          |           0         |           0        |  0 |
|                               |        0         |  0          |                0         |  0          |                      0          |           0         |           0        |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | n/a | n/a | 15 |
| no_crisis | anxiety_crisis | 0.150 | 113 |
| risk_taking_behaviours | suicidal_ideation | 1.000 | 1 |
| self-harm | suicidal_ideation | 0.118 | 17 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.059 | 17 |
| suicidal_ideation |  | 0.135 | 37 |
| violent_thoughts | risk_taking_behaviours | 0.167 | 6 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| risk_taking_behaviours | suicidal_ideation | 1.000 | 1.000 | 0.000 |
| risk_taking_behaviours | violent_thoughts | 0.167 | 0.000 | 0.167 |
| anxiety_crisis | no_crisis | 0.150 | 0.000 | 0.150 |
| self-harm | suicidal_ideation | 0.118 | 0.118 | 0.000 |
| no_crisis | suicidal_ideation | 0.080 | 0.053 | 0.027 |

### `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json`:
	* 🟩 Agreement Rate: 94.17%
	* 🧠 Cohen's Kappa: 0.92
Confusion Matrix between `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               32 |           0 |                        0 |           0 |                               1 |                   0 |                  0 |  1 |
| no_crisis                     |                2 |          77 |                        0 |           0 |                               0 |                   1 |                  0 |  2 |
| risk_taking_behaviours        |                0 |           0 |                        2 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           0 |                        0 |           0 |                               0 |                  43 |                  0 |  0 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           2 |                        0 |           0 |                               0 |                   2 |                  0 |  3 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.0243902 |                        0 |           0 |                       0.0294118 |           0         |                  0 |  0 |
| no_crisis                     |        0.0243902 |   0         |                        0 |           0 |                       0.0526316 |           0.0121951 |                  0 |  0 |
| risk_taking_behaviours        |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| self-harm                     |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| substance_abuse_or_withdrawal |        0.0294118 |   0.0526316 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| suicidal_ideation             |        0         |   0.0121951 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| violent_thoughts              |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
|                               |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | substance_abuse_or_withdrawal | 0.029 | 34 |
| no_crisis | anxiety_crisis | 0.024 | 82 |
| risk_taking_behaviours | n/a | n/a | 2 |
| self-harm | n/a | n/a | 14 |
| substance_abuse_or_withdrawal | no_crisis | 0.053 | 19 |
| suicidal_ideation | n/a | n/a | 43 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | substance_abuse_or_withdrawal | 0.053 | 0.000 | 0.053 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.029 | 0.029 | 0.000 |
| anxiety_crisis | no_crisis | 0.024 | 0.000 | 0.024 |
| no_crisis | suicidal_ideation | 0.012 | 0.012 | 0.000 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |

### `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 91.26%
	* 🧠 Cohen's Kappa: 0.88
Confusion Matrix between `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               32 |           1 |                        0 |           0 |                               0 |                   0 |                  0 |  1 |
| no_crisis                     |                1 |          77 |                        0 |           0 |                               0 |                   0 |                  0 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        2 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                0 |           1 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           2 |                        0 |           0 |                               0 |                  38 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           3 |                        0 |           0 |                               0 |                   2 |                  0 |  2 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.0416069 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| no_crisis                     |        0.0416069 |   0         |                        0 |           0 |                       0.0526316 |           0.0465116 |                  0 |  0 |
| risk_taking_behaviours        |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| self-harm                     |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| substance_abuse_or_withdrawal |        0         |   0.0526316 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| suicidal_ideation             |        0         |   0.0465116 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| violent_thoughts              |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
|                               |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.029 | 34 |
| no_crisis |  | 0.049 | 82 |
| risk_taking_behaviours | n/a | n/a | 2 |
| self-harm | n/a | n/a | 14 |
| substance_abuse_or_withdrawal | no_crisis | 0.053 | 19 |
| suicidal_ideation |  | 0.070 | 43 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | substance_abuse_or_withdrawal | 0.053 | 0.000 | 0.053 |
| no_crisis | suicidal_ideation | 0.047 | 0.000 | 0.047 |
| anxiety_crisis | no_crisis | 0.042 | 0.029 | 0.012 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |
| anxiety_crisis | self-harm | 0.000 | 0.000 | 0.000 |

### `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json`:
	* 🟩 Agreement Rate: 92.23%
	* 🧠 Cohen's Kappa: 0.90
Confusion Matrix between `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json` (ROWS) and `meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json` (COLS):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |               32 |           2 |                        0 |           0 |                               0 |                   0 |                  0 |  0 |
| no_crisis                     |                0 |          76 |                        0 |           0 |                               0 |                   0 |                  0 |  4 |
| risk_taking_behaviours        |                0 |           0 |                        2 |           0 |                               0 |                   0 |                  0 |  0 |
| self-harm                     |                0 |           0 |                        0 |          14 |                               0 |                   0 |                  0 |  0 |
| substance_abuse_or_withdrawal |                1 |           0 |                        0 |           0 |                              18 |                   0 |                  0 |  0 |
| suicidal_ideation             |                0 |           3 |                        0 |           0 |                               0 |                  40 |                  0 |  3 |
| violent_thoughts              |                0 |           0 |                        0 |           0 |                               0 |                   0 |                  5 |  0 |
|                               |                0 |           3 |                        0 |           0 |                               0 |                   0 |                  0 |  3 |

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |        0         |   0.0588235 |                        0 |           0 |                       0.0526316 |           0         |                  0 |  0 |
| no_crisis                     |        0.0588235 |   0         |                        0 |           0 |                       0         |           0.0652174 |                  0 |  0 |
| risk_taking_behaviours        |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| self-harm                     |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| substance_abuse_or_withdrawal |        0.0526316 |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| suicidal_ideation             |        0         |   0.0652174 |                        0 |           0 |                       0         |           0         |                  0 |  0 |
| violent_thoughts              |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |
|                               |        0         |   0         |                        0 |           0 |                       0         |           0         |                  0 |  0 |

Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.059 | 34 |
| no_crisis |  | 0.050 | 80 |
| risk_taking_behaviours | n/a | n/a | 2 |
| self-harm | n/a | n/a | 14 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.053 | 19 |
| suicidal_ideation | no_crisis | 0.065 | 46 |
| violent_thoughts | n/a | n/a | 5 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | suicidal_ideation | 0.065 | 0.000 | 0.065 |
| anxiety_crisis | no_crisis | 0.059 | 0.059 | 0.000 |
| anxiety_crisis | substance_abuse_or_withdrawal | 0.053 | 0.000 | 0.053 |
| anxiety_crisis | risk_taking_behaviours | 0.000 | 0.000 | 0.000 |
| anxiety_crisis | self-harm | 0.000 | 0.000 | 0.000 |

## Inter-Rater Agreement
- Fleiss' Kappa (across all human annotators): 0.549

- Fleiss' Kappa (across all LLM annotators): 0.805

- Fleiss' Kappa (across gpt-4o-mini): 0.944

- Fleiss' Kappa (across gpt-5-nano): 0.866

- Fleiss' Kappa (across meta-llama-Llama-4-Scout-17B-16E-Instruct): 0.902

## Human vs LLM Rater Agreement
| Human | LLM type | Avg Agreement Rate (%) | Avg Cohen's Kappa |
|-------|---------|---------------------|----------------|
| H1_labeled_n206_s42.json | gpt-4o-mini (n=3)| 72.330 | 0.643 |
| H1_labeled_n206_s42.json | gpt-5-nano (n=3)| 67.799 | 0.583 |
| H1_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct (n=3)| 68.123 | 0.595 |
| H2_labeled_n206_s42.json | gpt-4o-mini (n=3)| 85.113 | 0.780 |
| H2_labeled_n206_s42.json | gpt-5-nano (n=3)| 84.466 | 0.764 |
| H2_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct (n=3)| 76.861 | 0.678 |
| H3_labeled_n206_s42.json | gpt-4o-mini (n=3)| 64.239 | 0.538 |
| H3_labeled_n206_s42.json | gpt-5-nano (n=3)| 64.401 | 0.536 |
| H3_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct (n=3)| 61.974 | 0.517 |
| H4_labelled_n206_s42.json | gpt-4o-mini (n=3)| 72.816 | 0.617 |
| H4_labelled_n206_s42.json | gpt-5-nano (n=3)| 74.919 | 0.639 |
| H4_labelled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct (n=3)| 65.372 | 0.534 |
## Summary of Agreement Rates
| Rater 1 | Rater 2 | Agreement Rate (%) | Cohen's Kappa |
|---------|---------|---------------------|----------------|
| H1_labeled_n206_s42.json | H2_labeled_n206_s42.json | 67.476 | 0.576 |
| H1_labeled_n206_s42.json | H3_labeled_n206_s42.json | 67.476 | 0.591 |
| H1_labeled_n206_s42.json | H4_labelled_n206_s42.json | 57.767 | 0.460 |
| H1_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | 73.301 | 0.656 |
| H1_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | 71.845 | 0.637 |
| H1_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 71.845 | 0.637 |
| H1_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 70.874 | 0.622 |
| H1_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 66.019 | 0.561 |
| H1_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 66.505 | 0.566 |
| H1_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 67.476 | 0.586 |
| H1_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 68.932 | 0.605 |
| H1_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 67.961 | 0.593 |
| H2_labeled_n206_s42.json | H3_labeled_n206_s42.json | 64.078 | 0.530 |
| H2_labeled_n206_s42.json | H4_labelled_n206_s42.json | 71.845 | 0.590 |
| H2_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | 85.437 | 0.785 |
| H2_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | 84.951 | 0.777 |
| H2_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 84.951 | 0.779 |
| H2_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 85.437 | 0.783 |
| H2_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 82.524 | 0.734 |
| H2_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 85.437 | 0.776 |
| H2_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 76.699 | 0.676 |
| H2_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 77.184 | 0.684 |
| H2_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 76.699 | 0.675 |
| H3_labeled_n206_s42.json | H4_labelled_n206_s42.json | 66.505 | 0.570 |
| H3_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | 64.563 | 0.542 |
| H3_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | 63.592 | 0.529 |
| H3_labeled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 64.563 | 0.542 |
| H3_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 66.019 | 0.558 |
| H3_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 62.621 | 0.513 |
| H3_labeled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 64.563 | 0.538 |
| H3_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 61.650 | 0.513 |
| H3_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 62.621 | 0.525 |
| H3_labeled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 61.650 | 0.513 |
| H4_labelled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | 73.301 | 0.623 |
| H4_labelled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | 73.301 | 0.622 |
| H4_labelled_n206_s42.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 71.845 | 0.604 |
| H4_labelled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 74.272 | 0.634 |
| H4_labelled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 73.786 | 0.622 |
| H4_labelled_n206_s42.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 76.699 | 0.660 |
| H4_labelled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 65.534 | 0.536 |
| H4_labelled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 65.049 | 0.531 |
| H4_labelled_n206_s42.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 65.534 | 0.535 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | 97.087 | 0.958 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 96.117 | 0.945 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 89.806 | 0.853 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 87.864 | 0.822 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 89.806 | 0.849 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 83.981 | 0.782 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 84.466 | 0.789 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250818-164149.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 83.981 | 0.781 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | 95.146 | 0.931 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 88.350 | 0.831 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 86.893 | 0.807 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 89.320 | 0.841 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 83.495 | 0.774 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 83.981 | 0.782 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-120514.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 82.524 | 0.761 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | 88.350 | 0.832 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 87.379 | 0.816 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 87.379 | 0.814 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 82.039 | 0.756 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 83.495 | 0.776 |
| gpt-4o-mini-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-121533.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 81.068 | 0.742 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | 91.262 | 0.871 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 89.806 | 0.847 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 79.612 | 0.720 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 80.583 | 0.734 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-122630.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 78.155 | 0.699 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | 92.233 | 0.881 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 80.097 | 0.724 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 81.068 | 0.739 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-123814.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 79.126 | 0.710 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | 79.126 | 0.709 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 79.126 | 0.710 |
| gpt-5-nano-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250819-124909.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 79.126 | 0.709 |
| meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | 94.175 | 0.923 |
| meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130636.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 91.262 | 0.884 |
| meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-130838.json | meta-llama-Llama-4-Scout-17B-16E-Instruct-labeled-sampled_dataset_n_200_merged_n50-noSeed_156-s42-20250820-131430.json | 92.233 | 0.897 |
---
## Summary of Most Confused Labels (Overall)
- Rater pairs: 78

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |       0          |   0.417056  |                0.0203561 |  0.00386378 |                      0.0375751  |          0.0704167  |         0.00405186 |  0 |
| no_crisis                     |       0.417056   |   0         |                0.485289  |  0.074439   |                      0.0403843  |          0.092737   |         0.142723   |  0 |
| risk_taking_behaviours        |       0.0203561  |   0.485289  |                0         |  0.0927944  |                      0.13031    |          0.229726   |         0.0798415  |  0 |
| self-harm                     |       0.00386378 |   0.074439  |                0.0927944 |  0          |                      0.0272206  |          0.100251   |         0.0241758  |  0 |
| substance_abuse_or_withdrawal |       0.0375751  |   0.0403843 |                0.13031   |  0.0272206  |                      0          |          0.00832364 |         0.0021978  |  0 |
| suicidal_ideation             |       0.0704167  |   0.092737  |                0.229726  |  0.100251   |                      0.00832364 |          0          |         0.0746876  |  0 |
| violent_thoughts              |       0.00405186 |   0.142723  |                0.0798415 |  0.0241758  |                      0.0021978  |          0.0746876  |         0          |  0 |
|                               |       0          |   0         |                0         |  0          |                      0          |          0          |         0          |  0 |


Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.336 | 2468 |
| no_crisis | anxiety_crisis | 0.081 | 7122 |
| risk_taking_behaviours | no_crisis | 0.480 | 427 |
| self-harm | suicidal_ideation | 0.083 | 1396 |
| substance_abuse_or_withdrawal | anxiety_crisis | 0.032 | 1300 |
| suicidal_ideation | no_crisis | 0.057 | 2856 |
| violent_thoughts | no_crisis | 0.136 | 455 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.485 | 0.005 | 0.480 |
| anxiety_crisis | no_crisis | 0.417 | 0.336 | 0.081 |
| risk_taking_behaviours | suicidal_ideation | 0.230 | 0.225 | 0.005 |
| no_crisis | violent_thoughts | 0.143 | 0.006 | 0.136 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.130 | 0.126 | 0.004 |
---
## Summary of Most Confused Labels (Humans vs Humans)
- Rater pairs: 6

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |       0          |   0.595788  |                0.0490498 |   0.0185185 |                      0.0189394  |          0.0917549  |         0.00757576 |  0 |
| no_crisis                     |       0.595788   |   0         |                0.408898  |   0.115898  |                      0.107367   |          0.0957709  |         0.122134   |  0 |
| risk_taking_behaviours        |       0.0490498  |   0.408898  |                0         |   0.0616761 |                      0.223255   |          0.266497   |         0.0677966  |  0 |
| self-harm                     |       0.0185185  |   0.115898  |                0.0616761 |   0         |                      0.0185185  |          0.11201    |         0.0294118  |  0 |
| substance_abuse_or_withdrawal |       0.0189394  |   0.107367  |                0.223255  |   0.0185185 |                      0          |          0.00485437 |         0          |  0 |
| suicidal_ideation             |       0.0917549  |   0.0957709 |                0.266497  |   0.11201   |                      0.00485437 |          0          |         0.249857   |  0 |
| violent_thoughts              |       0.00757576 |   0.122134  |                0.0677966 |   0.0294118 |                      0          |          0.249857   |         0          |  0 |
|                               |       0          |   0         |                0         |   0         |                      0          |          0          |         0          |  0 |


Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.496 | 264 |
| no_crisis | anxiety_crisis | 0.100 | 472 |
| risk_taking_behaviours | no_crisis | 0.356 | 59 |
| self-harm | no_crisis | 0.093 | 108 |
| substance_abuse_or_withdrawal | no_crisis | 0.097 | 93 |
| suicidal_ideation | anxiety_crisis | 0.073 | 206 |
| violent_thoughts | suicidal_ideation | 0.235 | 34 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| anxiety_crisis | no_crisis | 0.596 | 0.496 | 0.100 |
| no_crisis | risk_taking_behaviours | 0.409 | 0.053 | 0.356 |
| risk_taking_behaviours | suicidal_ideation | 0.266 | 0.203 | 0.063 |
| suicidal_ideation | violent_thoughts | 0.250 | 0.015 | 0.235 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.223 | 0.169 | 0.054 |
---
## Summary of Most Confused Labels (LLMs vs Humans)
- Rater pairs: 36

s_balanced matrix (s(i,j) = P(j\|i) + P(i\|j)):
|                               |   anxiety_crisis |   no_crisis |   risk_taking_behaviours |   self-harm |   substance_abuse_or_withdrawal |   suicidal_ideation |   violent_thoughts |    |
|:------------------------------|-----------------:|------------:|-------------------------:|------------:|--------------------------------:|--------------------:|-------------------:|---:|
| anxiety_crisis                |       0          |   0.515521  |                0.014245  |  0.00447427 |                      0.0371709  |           0.107958  |         0.0059657  |  0 |
| no_crisis                     |       0.515521   |   0         |                0.523689  |  0.105338   |                      0.0475061  |           0.122601  |         0.247773   |  0 |
| risk_taking_behaviours        |       0.014245   |   0.523689  |                0         |  0.0950081  |                      0.125356   |           0.234412  |         0.0493827  |  0 |
| self-harm                     |       0.00447427 |   0.105338  |                0.0950081 |  0          |                      0.0289855  |           0.094502  |         0.0411523  |  0 |
| substance_abuse_or_withdrawal |       0.0371709  |   0.0475061 |                0.125356  |  0.0289855  |                      0          |           0.0177656 |         0.00411523 |  0 |
| suicidal_ideation             |       0.107958   |   0.122601  |                0.234412  |  0.094502   |                      0.0177656  |           0         |         0.0916814  |  0 |
| violent_thoughts              |       0.0059657  |   0.247773  |                0.0493827 |  0.0411523  |                      0.00411523 |           0.0916814 |         0          |  0 |
|                               |       0          |   0         |                0         |  0          |                      0          |           0         |         0          |  0 |


Most confused labels (row-normalized P(B\|A)):
| Label A | Most Confused As B | P(B\|A) | Support |
|---------|---------------------|--------|---------|
| anxiety_crisis | no_crisis | 0.424 | 1341 |
| no_crisis | anxiety_crisis | 0.091 | 3015 |
| risk_taking_behaviours | no_crisis | 0.521 | 351 |
| self-harm | no_crisis | 0.093 | 621 |
| substance_abuse_or_withdrawal | no_crisis | 0.036 | 585 |
| suicidal_ideation | no_crisis | 0.084 | 1260 |
| violent_thoughts | no_crisis | 0.243 | 243 |

Most confused label pairs (s_balanced):
| Label i | Label j | s_balanced | P(j\|i) | P(i\|j) |
|---------|---------|-----------:|-------:|-------:|
| no_crisis | risk_taking_behaviours | 0.524 | 0.002 | 0.521 |
| anxiety_crisis | no_crisis | 0.516 | 0.424 | 0.091 |
| no_crisis | violent_thoughts | 0.248 | 0.005 | 0.243 |
| risk_taking_behaviours | suicidal_ideation | 0.234 | 0.234 | 0.001 |
| risk_taking_behaviours | substance_abuse_or_withdrawal | 0.125 | 0.125 | 0.000 |
---