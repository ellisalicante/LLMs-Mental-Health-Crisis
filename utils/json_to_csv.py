import pandas as pd
df = pd.read_json(r"data\processed\sampled_dataset_n_200_merged_n50-noSeed_156-s42.json")
#df['inputs'] = df['inputs'].apply(lambda x: ' '.join(x))
df[['inputs','label']].to_csv("data.csv", index=False)