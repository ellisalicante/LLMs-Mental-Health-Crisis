import json
from math import sqrt
import pandas as pd
import os
import numpy as np


def load_json_to_df(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    keep = [c for c in ["evaluation", "evaluation_std", "label", "dataset_id"] if c in df.columns]
    df = df[keep].copy()
    df["source_file"] = os.path.basename(path)
    return df

def parse_filename(fname):
    parts = fname.split("_")
    evaluator = parts[0]
    responder = parts[1]
    dataset = "_".join(parts[2:-1])
    return evaluator, responder, dataset

def percentage_bins(series, bins=[0, 2.3333, 3.6666, 5], labels=None):
    valid = series.dropna()
    if valid.empty:
        if labels is None:
            labels = [f"[{bins[i]}, {bins[i+1]}]" for i in range(len(bins)-1)]
        return {lab: 0.0 for lab in labels}
    if labels is None:
        labels = [f"[{bins[i]}, {bins[i+1]}]" for i in range(len(bins)-1)]
    categories = pd.cut(valid, bins=bins, labels=labels, include_lowest=True, right=True)
    counts = categories.value_counts(normalize=True).sort_index() * 100
    return counts.to_dict()

def mean_ci_pm(series, conf=0.95):
    series = series.dropna()
    n = len(series)
    if n == 0:
        return np.nan, np.nan
    mean = series.mean()
    std = series.std(ddof=1)
    se = std / np.sqrt(n)
    z = 1.96  # 95% CI
    return mean, z * se

def proportion_ci_wilson(k, n, z=1.96):
    """Wilson score interval for binomial proportion; returns (p, low, high)."""
    if n == 0:
        return np.nan, np.nan, np.nan
    p = k / n
    denom = 1 + z**2 / n
    center = (p + z**2/(2*n)) / denom
    halfw = z * sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return p, center - halfw, center + halfw