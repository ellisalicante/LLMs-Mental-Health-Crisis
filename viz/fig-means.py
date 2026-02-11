import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Recreate the DataFrame from the table data
data = {
    'LLM': ['gpt-4o-mini', 'gpt-5-nano', 'llama-4-scout', 'deepseek-v3.2', 'grok-4-fast'],
    'Mean Score': [4.548, 4.936, 4.722, 4.915, 4.748],
    'Mean Score CI': [0.017, 0.008, 0.016, 0.010, 0.020],
    'Mean Std': [0.048, 0.019, 0.041, 0.017, 0.028],
    'Mean Std CI': [0.004, 0.002, 0.003, 0.030, 0.030],
    '1': [0.47, 0.26, 0.80, 0.51, 2.79],
    '[1, 2.3]': [1.09, 0.50, 1.71, 0.77, 4.21],
    '(2.3, 3.6]': [6.88, 0.20, 1.99, 1.09, 5.23],
    '(3.6, 5]': [92.03, 99.30, 96.30, 98.91, 94.77]
}

df = pd.DataFrame(data)

# --- 2. Implement the Custom Order ---
NEW_LLM_ORDER = [
    'grok-4-fast',
    'gpt-4o-mini', 
    'llama-4-scout', 
    'gpt-5-nano', 
    'deepseek-v3.2'
]

llm_type = pd.CategoricalDtype(categories=NEW_LLM_ORDER, ordered=True)
df['LLM'] = df['LLM'].astype(llm_type)
df_sorted = df.sort_values('LLM').reset_index(drop=True)

# 3. Set up the plotting style for paper inclusion
try:
    plt.style.use(['science', 'no-latex'])
    plt.rcParams.update({'font.family': 'serif', 'font.size': 12})
except:
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 14,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'legend.fontsize': 12,
        'figure.figsize': (12, 3)
    })

fig, axes = plt.subplots(1, 3, figsize=(11, 3))
bar_width = 0.9

# --- Plot 1: Mean Score ---
ax1 = axes[0]
ax1.bar(
    df_sorted['LLM'],
    df_sorted['Mean Score'],
    width=bar_width,
    yerr=df_sorted['Mean Score CI'],
    capsize=4,
    color="#ACACAC",
    linewidth=0.,
    edgecolor='black'
)
ax1.set_title('(a) Mean Score', pad=10)
ax1.set_ylabel('Mean Score')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.set_ylim(4.0, 5.0)

# --- Plot 2: Mean Std ---
ax2 = axes[1]
ax2.bar(
    df_sorted['LLM'],
    df_sorted['Mean Std'],
    width=bar_width,
    yerr=df_sorted['Mean Std CI'],
    capsize=4,
    color="#ACACAC",
    linewidth=0.,
    edgecolor='black'
)
ax2.set_title('(b) Mean Std')
ax2.set_ylabel('Mean Std')
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.set_ylim(0, None) 

# --- Plot 3: Stacked Low-Score Distribution ---
ax3 = axes[2]

# Calculate the bottoms for the stack, starting at y=0
bottom_bin1 = 0 
bottom_bin2 = df_sorted['[1, 2.3]'] # bottom of the (2.3, 3.6] bin

# 1. [1, 2.3] bin (Bottom Stack)
ax3.bar(
    df_sorted['LLM'],
    df_sorted['[1, 2.3]'],
    width=bar_width,
    bottom=bottom_bin1,
    label='[1, 2.3]',
    color="#E7951A"
)
# 2. (2.3, 3.6] bin (Stacked on top)
ax3.bar(
    df_sorted['LLM'],
    df_sorted['(2.3, 3.6]'],
    width=bar_width,
    bottom=bottom_bin2,
    label='(2.3, 3.6]',
    color="#6590E0"
)
# 3. Score = 1 (Hatched overlay - Starts at y=0, overlapping the [1, 2.3] bar)
ax3.bar(
    df_sorted['LLM'],
    df_sorted['1'],
    width=bar_width,
    bottom=0,
    label='Score = 1',
    hatch='/////',
    facecolor='none',
    edgecolor='#A5002A',
    linewidth=1 
)

ax3.set_title('(c) Low-Score Distribution', pad=10)
ax3.set_ylabel('Percentage (%)')
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# Set y-limit to focus on the low bins
max_low_score = (df_sorted['[1, 2.3]'] + df_sorted['(2.3, 3.6]']).max()
ax3.set_ylim(0, max_low_score * 1.1)

# Adjust legend order: (2.3, 3.6], [1, 2.3], Score = 1
handles, labels = ax3.get_legend_handles_labels()
# Plot order: [1, 2.3], (2.3, 3.6], Score = 1. Desired indices: [1, 0, 2]
order = [1, 0, 2] 

ax3.legend(
    [handles[idx] for idx in order],
    [labels[idx] for idx in order],
    frameon=True, fontsize=10, loc='upper right'
)


# --- Final Adjustments ---
for ax in axes:
    plt.setp(ax.get_xticklabels(), rotation=25, ha='right')

plt.tight_layout()
plt.savefig('results-llm-aggregated.png', dpi=300)
#also pdf
plt.savefig('results-llm-aggregated.pdf', dpi=300, format='pdf', bbox_inches='tight', pad_inches=0.1)
plt.close()