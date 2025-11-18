#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.stat_utils import (
    load_json_to_df,
    parse_filename,
    percentage_bins,
    mean_ci_pm,
    proportion_ci_wilson
)

# --- Try to use the 'science' style (requires scienceplots); fall back if missing
sns.set_style("whitegrid")
try:
    import scienceplots  # noqa: F401
    plt.style.use(['science'])
except Exception:
    plt.rcParams.update({
        "figure.figsize": (6.5, 4.0),
        "axes.grid": True,
        "grid.alpha": 0.25,
        "font.size": 11,
    })
    # global qualitative palette
    plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#d95f02", "#7570b3", "#1b9e77", "#e7298a", "#66a61e"]
    )

parser = argparse.ArgumentParser(description="Compute evaluation statistics and save figures")
parser.add_argument("--input-files", nargs="+", help="Paths to the input JSON files")
args = parser.parse_args()
files = args.input_files
assert files, "Need at least one file to compute statistics"

FIG_DIR = "outputs"
os.makedirs(FIG_DIR, exist_ok=True)

BINS = [0.0, 2.3333, 3.6666, 5.0]
BIN_LABELS = ["[0-2.3]", "(2.3-3.6]", "(3.6-5]"]

# Map long responder IDs to pretty display names
MODEL_NAME_MAP = {
    "meta-llama-Llama-4-Scout-17B-16E-Instruct-answers-sampled": "llama-4-Scout",
    "gpt-5-nano-answers-sampled": "gpt-5-nano",
    "gpt-4o-mini-answers-sampled": "gpt-4o-mini",
     "grok-4-fast-non-reasoning-answers-sampled": "grok-4-fast",
     "deepseek-chat-answers-sampled": "deepseek-v3.2",
}
# Optional: pretty names + order for labels
LABEL_NAME_MAP = {
    "no_crisis": "no-crisis",
    "anxiety_crisis": "anxiety-crisis",
    "risk_taking_behaviours": "risk-taking",
    "self-harm": "self-harm",
    "substance_abuse_or_withdrawal": "substance-use/withdrawal",
    "suicidal_ideation": "suicidal-ideation",
    "violent_thoughts": "violent-thoughts",
}
LABEL_ORDER = [
    "no-crisis", "anxiety-crisis", "risk-taking",
    "self-harm", "substance-use/withdrawal",
    "suicidal-ideation", "violent-thoughts",
]


# ----------------- load & annotate -----------------

df_all = pd.concat([load_json_to_df(f) for f in files], ignore_index=True)

df_all[["evaluator","responder","dataset"]] = df_all["source_file"].apply(
    lambda f: pd.Series(parse_filename(f))
)
df_all["responder_pretty"] = df_all["responder"].apply(lambda x: MODEL_NAME_MAP[x])

# pretty + ordered labels
df_all["label_pretty"] = df_all["label"].map(LABEL_NAME_MAP).fillna(df_all["label"])
df_all["label_pretty"] = pd.Categorical(df_all["label_pretty"], categories=LABEL_ORDER, ordered=True)

# ----------------- per-file stats (printed) -----------------

print("# Individual file analysis")
rows = []
for f, g in df_all.groupby("source_file"):
    responder = g["responder_pretty"].iloc[0]
    dataset = g["dataset"].iloc[0]

    mean_eval, hw_eval = mean_ci_pm(g["evaluation"])
    mean_std, hw_std   = mean_ci_pm(g["evaluation_std"])
    bin_perc = percentage_bins(g["evaluation"], bins=BINS, labels=BIN_LABELS)
    row = {
        "File": f"{responder}-{dataset}",
        "N": g["evaluation"].notna().sum(),
        "Mean Std devs": f"{mean_std:.3f} $\\pm$ {hw_std:.3f}",
        "Mean Evaluations": f"{mean_eval:.3f} $\\pm$ {hw_eval:.3f}",
        "eval=1": (g["evaluation"].eq(1).mean()*100),
        **{f" & {label}": f"{perc:.2f}" for label, perc in bin_perc.items()}
    }
    rows.append(row)

df_individual = pd.DataFrame(rows)
print(df_individual.to_string(index=False))

# ----------------- together stats (printed) -----------------

print("\n# Together file analysis")
mean_eval, hw_eval = mean_ci_pm(df_all["evaluation"])
mean_std, hw_std   = mean_ci_pm(df_all["evaluation_std"])
bin_perc = percentage_bins(df_all["evaluation"], bins=BINS, labels=BIN_LABELS)
row = {
    "Responder": df_all["responder_pretty"].iloc[0],
    "N": df_all["evaluation"].notna().sum(),
    "Mean Std devs": f"{mean_std:.3f} $\\pm$ {hw_std:.3f}",
    "Mean Evaluations": f"{mean_eval:.3f} $\\pm$ {hw_eval:.3f}",
    "eval=1": (df_all["evaluation"].eq(1).mean()*100),
    **{f" & {label}": f"{perc:.2f}" for label, perc in bin_perc.items()}
}
df_total = pd.DataFrame([row])
print(df_total.to_string(index=False))

# ----------------- aggregate by PRETTY responder (for plots & CSV) -----------------

summary_rows = []
for model, g in df_all.groupby("responder_pretty"):
    valid = g["evaluation"].notna()
    evals = g.loc[valid, "evaluation"]
    stds  = g.loc[valid, "evaluation_std"] if "evaluation_std" in g else pd.Series(dtype=float)

    mean_eval_m, hw_eval_m = mean_ci_pm(evals)
    mean_std_m,  hw_std_m  = mean_ci_pm(stds)
    dist = percentage_bins(evals, bins=BINS, labels=BIN_LABELS)

    summary_rows.append({
        "Model": model,
        "Num examples": int(valid.sum()),
        "Mean Evaluations (mean)": mean_eval_m,
        "Mean Evaluations (±95%CI)": hw_eval_m,
        "Mean Std devs (mean)": mean_std_m,
        "Mean Std devs (±95%CI)": hw_std_m,
        "eval=1": float(evals.eq(1).mean() * 100.0) if len(evals) else np.nan,
        BIN_LABELS[0] : dist.get(BIN_LABELS[0], 0.0),
        BIN_LABELS[1] : dist.get(BIN_LABELS[1], 0.0),
        BIN_LABELS[2] : dist.get(BIN_LABELS[2], 0.0),
    })

summary = pd.DataFrame(summary_rows).sort_values("Model").reset_index(drop=True)
summary_path = os.path.join(FIG_DIR, "evaluation_summary.csv")
summary.to_csv(summary_path, index=False)
print(f"\nSaved summary CSV → {summary_path}")
print(summary)

# ----------------- breakdown by model × label -----------------
print("\n# Breakdown by Model × Label")
rows = []
for (model, label), g in df_all.groupby(["responder_pretty", "label_pretty"]):
    evals = g["evaluation"].dropna()
    if evals.empty:
        continue

    # Risk P(eval=1 | model, label) with Wilson 95% CI
    k = int((evals == 1).sum())
    n = int(evals.size)
    p, plo, phi = proportion_ci_wilson(k, n)
    risk_pct, risk_low, risk_high = 100 * p, 100 * plo, 100 * phi

    # Bin distribution
    dist = percentage_bins(evals, bins=BINS, labels=BIN_LABELS)

    mean_eval, hw_eval = mean_ci_pm(evals)
    mean_std,  hw_std  = mean_ci_pm(g["evaluation_std"].dropna())

    rows.append({
        "Model": model,
        "Label": label,
        "N": n,
        "Mean Eval": f"{mean_eval:.3f} \\tiny{{$\\pm$ {hw_eval:.3f}}}",
        "Mean Std": f"{mean_std:.3f} \\tiny{{$\\pm$ {hw_std:.3f}}}",
        "eval=1": f"{risk_pct:.2f}",
        "eval=1 WI": f"[{risk_low:.2f}, {risk_high:.2f}]",
        **{f"{bin_label}": f"{dist.get(bin_label, 0.0):.2f}" for bin_label in dist},
    })

df_model_label = pd.DataFrame(rows).sort_values(["Model", "Label"]).reset_index(drop=True)
print(df_model_label.to_string(index=False))

label_summary_path = os.path.join(FIG_DIR, "evaluation_by_label.csv")
df_model_label.to_csv(label_summary_path, index=False)
print(f"\nSaved breakdown by model × label CSV → {label_summary_path}")

# ----------------- FIGURES (saved as PDFs) -----------------

# x-ticks based on pretty model names
x = np.arange(len(summary))
tick_labels = summary["Model"].tolist()

# 1) Mean Evaluations with error bars
plt.figure()
y = summary["Mean Evaluations (mean)"].values
yerr = summary["Mean Evaluations (±95%CI)"].values
plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=4)
plt.xticks(x, tick_labels, rotation=0)
plt.ylabel("Mean Evaluation (1-5)")
plt.title("Mean Evaluation by Model (±95% CI)")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mean_evaluations.pdf"))
plt.close()

# 2) Mean Std Devs with error bars
plt.figure()
y2 = summary["Mean Std devs (mean)"].values
y2err = summary["Mean Std devs (±95%CI)"].values
plt.errorbar(x, y2, yerr=y2err, fmt='o', capsize=4)
plt.xticks(x, tick_labels, rotation=0)
plt.title("Mean Std Dev (Evaluator Agreement per model answers)")
plt.xlabel("Model Responding")
plt.ylabel("Mean Std Dev by Model (±95% CI)")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "mean_stddevs.pdf"))
plt.close()

# 3) Stacked bar distribution across bins
plt.figure()
width = 0.6
a = summary[BIN_LABELS[0]].values
b = summary[BIN_LABELS[1]].values
c = summary[BIN_LABELS[2]].values

# Dedicated palette for bins (R-O-G)
colors = ["#d7191c", "#fdae61", "#1a9641"]
p1 = plt.bar(x, a, width, color=colors[0])
p2 = plt.bar(x, b, width, bottom=a, color=colors[1])
p3 = plt.bar(x, c, width, bottom=a+b, color=colors[2])
plt.xticks(x, tick_labels, rotation=0)
plt.ylabel("Percentage of Evaluations")
plt.title("Score Distribution by Model")
plt.legend([p1[0], p2[0], p3[0]], BIN_LABELS, title="Bins")
#log scale on y
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "score_distribution.pdf"))
plt.close()

# 4) % with score == 1
plt.figure()
y3 = summary["eval=1"].values
plt.bar(x, y3, width=0.6, color=colors[0])
plt.xticks(x, tick_labels, rotation=0)
plt.ylabel(r"\% with score == 1")
plt.title("Severely Harmful Cases (score == 1)")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "score_eq1.pdf"))
plt.close()


# ---- 5) Heatmap of harmful % (eval=1) ----


# Ensure numeric columns are actually numeric (they were stored as strings with ± in table)
df_viz = df_model_label.copy()
df_viz["eval=1"] = df_viz["eval=1"].astype(float)
for col in BIN_LABELS:
    df_viz[col] = df_viz[col].astype(float)

# Extract numeric mean evaluations (before ±) for plotting
df_viz["mean_eval_num"] = df_viz["Mean Eval"].str.extract(r"^([\d\.]+)").astype(float)
df_viz["mean_std_num"] = df_viz["Mean Std"].str.extract(r"^([\d.]+)").astype(float)


pivot = df_viz.pivot(index="Label", columns="Model", values="eval=1")
plt.figure(figsize=(7,5))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="Reds", cbar_kws={'label': '% eval=1'})
plt.title("Harmful Answer Rate (P(eval=1|label,model))")
plt.ylabel("Label")
plt.xlabel("Model")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "heatmap_eval1.pdf"))
plt.close()

# ---- 6) Grouped bar: Mean evaluation per label with ±95% CI ----
labels = df_viz["Label"].unique()
models = df_viz["Model"].unique()
x = np.arange(len(labels))
width = 0.25  # width of bars

fig, ax = plt.subplots(figsize=(9,5))

for i, model in enumerate(models):
    subset = df_all[df_all["responder_pretty"] == model]
    means, cis = [], []
    for label in LABEL_ORDER:
        data = subset.loc[subset["label_pretty"] == label, "evaluation"]
        if data.empty:
            means.append(np.nan)
            cis.append(np.nan)
        else:
            mean, hw = mean_ci_pm(data)
            means.append(mean)
            cis.append(hw)
    means = np.array(means)
    cis = np.array(cis)
    ax.bar(x + i*width, means, width, yerr=cis, capsize=4, label=model)

ax.set_xticks(x + width * (len(models)-1) / 2)
ax.set_xticklabels(labels, rotation=8, ha="center")
ax.set_ylabel("Mean Evaluation (1–5)")
ax.set_title("Mean Evaluation by Label and Model (±95% CI)")
ax.legend(title="Model")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "bar_meaneval_by_label_CI.pdf"))
plt.close()

# ---- 7) Stacked 100% bars: distribution across bins per label ----
bin_cols = BIN_LABELS
for model in df_viz["Model"].unique():
    subset = df_viz[df_viz["Model"]==model]
    x = np.arange(len(subset["Label"]))
    fig, ax = plt.subplots(figsize=(8,5))
    a = subset[bin_cols[0]].values
    b = subset[bin_cols[1]].values
    c = subset[bin_cols[2]].values
    ax.bar(x, a, width=0.6, label=bin_cols[0], color=colors[0])
    ax.bar(x, b, width=0.6, bottom=a, label=bin_cols[1], color=colors[1])
    ax.bar(x, c, width=0.6, bottom=a+b, label=bin_cols[2], color=colors[2])
    ax.set_xticks(x)
    ax.set_xticklabels(subset["Label"], rotation=8, ha="center")
    ax.set_ylabel("Percentage of Evaluations")
    #ax.set_ylim(0,100)
    ax.set_title(f"Score Distribution by Label ({model})")
    ax.legend(title="Bins")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, f"stacked_bins_{model}.pdf"))
    plt.close()

# ---- 8) Scatterplot: trade-off view ----
plt.figure(figsize=(7,5))
sns.scatterplot(data=df_viz, x="mean_eval_num", y="eval=1", hue="Model", style="Label", s=100)
plt.xlabel("Mean Evaluation")
plt.ylabel(r"\% eval=1 (Harmful)")
plt.title("Trade-off: Quality vs Harm by Label")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "scatter_tradeoff.pdf"))
plt.close()


# ---- 9) Scatterplot: Mean Eval vs Mean Std (Quality vs Consensus) ----
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df_viz,
    x="mean_eval_num",
    y="mean_std_num",   # numeric mean std we’ll extract below
    hue="Model",
    style="Label",
    s=100
)
plt.xlabel("Mean Evaluation")
plt.ylabel("Mean Std (Evaluator Consensus)")
plt.title("Trade-off: Quality vs Consensus by Label")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "scatter_eval_vs_std.pdf"))
plt.close()


# ---- 10) Scatterplot: % eval=1 vs Mean Std (Harm vs Consensus) ----
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df_viz,
    x="eval=1",
    y="mean_std_num",
    hue="Model",
    style="Label",
    s=100
)
plt.xlabel(r"\% eval=1 (Harmful)")
plt.ylabel("Mean Std (Evaluator Consensus)")
plt.title("Trade-off: Harm vs Consensus by Label")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "scatter_harm_vs_std.pdf"))
plt.close()


print(f"Saved PDFs in: {FIG_DIR}/")
