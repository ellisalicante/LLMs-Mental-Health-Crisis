import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Manually transcribed data from the LaTeX table
data = {
    'LLM': [
        'gpt-4o-mini', 'gpt-4o-mini', 'gpt-4o-mini', 'gpt-4o-mini', 'gpt-4o-mini', 'gpt-4o-mini', 'gpt-4o-mini',
        'gpt-5-nano', 'gpt-5-nano', 'gpt-5-nano', 'gpt-5-nano', 'gpt-5-nano', 'gpt-5-nano', 'gpt-5-nano',
        'llama-4-scout', 'llama-4-scout', 'llama-4-scout', 'llama-4-scout', 'llama-4-scout', 'llama-4-scout', 'llama-4-scout',
        'deepseek-v3.2', 'deepseek-v3.2', 'deepseek-v3.2', 'deepseek-v3.2', 'deepseek-v3.2', 'deepseek-v3.2', 'deepseek-v3.2',
        'grok-4-fast', 'grok-4-fast', 'grok-4-fast', 'grok-4-fast', 'grok-4-fast', 'grok-4-fast', 'grok-4-fast'
    ],
    'Category': [
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis',
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis',
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis',
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis',
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis'
    ],
    '1': [
        1.14, 2.88, 0.00, 0.00, 0.00, 0.00, 0.11,
        0.35, 1.20, 0.00, 0.00, 0.00, 0.00, 0.19,
        2.19, 4.80, 0.00, 1.59, 0.00, 0.00, 0.08,
        0.96, 1.92, 0.00, 0.00, 0.00, 0.00, 0.32,
        6.40, 17.51, 0.00, 3.17, 0.43, 14.04, 0.38
    ],
    '[1, 2.3]': [
        2.72, 5.04, 0.00, 0.00, 0.00, 0.00, 0.41,
        1.23, 1.68, 0.00, 0.00, 0.00, 5.26, 0.19,
        3.95, 12.95, 0.00, 4.76, 0.00, 0.00, 0.08,
        1.67, 3.12, 0.00, 0.00, 0.00, 0.00, 0.41,
        9.39, 28.30, 0.00, 7.94, 0.43, 21.05, 0.41
    ],
    '(2.3, 3.6]': [
        26.93, 17.75, 1.69, 3.17, 7.79, 10.53, 0.16,
        0.35, 0.72, 0.00, 0.00, 0.00, 1.75, 0.11,
        5.88, 7.91, 1.13, 1.59, 0.43, 10.53, 0.22,
        0.53, 1.68, 0.19, 0.00, 0.87, 0.00, 0.11,
        2.28, 6.47, 0.19, 6.35, 0.43, 7.02, 0.00
    ]
}

df = pd.DataFrame(data)

# --- Configuration for New Plot Structure ---
# Define and apply the new category order
NEW_CATEGORIES_ORDER = [
    'self-harm', 'suicidal ideation', 'risk-taking behaviors', 
    'violent thoughts', 'substance abuse', 'anxiety crisis', 'no crisis'
]
cat_type = pd.CategoricalDtype(categories=NEW_CATEGORIES_ORDER, ordered=True)
df['Category'] = df['Category'].astype(cat_type)

categories = NEW_CATEGORIES_ORDER
n_cat = len(categories)

# Define the new desired order of models:
NEW_LLM_ORDER = [
    'grok-4-fast',
    'gpt-4o-mini', 
    'llama-4-scout', 
    'gpt-5-nano', 
    'deepseek-v3.2'
]

llm_names = NEW_LLM_ORDER
n_llm = len(llm_names)

# Define LLM codes A-E (Keeping this map, but not using it for the top label)
llm_code_map = {
    'gpt-4o-mini': 'A',
    'gpt-5-nano': 'B',
    'llama-4-scout': 'C',
    'deepseek-v3.2': 'D',
    'grok-4-fast': 'E'
}

# Define Crisis Abbreviated Labels (Bottom x-axis tick labels)
CRISIS_ABBREV_MAP = {
    'self-harm': 'SH',
    'suicidal ideation': 'SI',
    'risk-taking behaviors': 'RTB',
    'violent thoughts': 'VT',
    'substance abuse': 'SA',
    'anxiety crisis': 'AC',
    'no crisis': 'NC'
}

# Collect all x-positions and labels for the new x-axis
all_x_positions = []
all_x_labels = []

# 2. Set up the plotting style
try:
    plt.style.use(['science', 'no-latex'])
    plt.rcParams.update({'font.family': 'serif', 'font.size': 12})
except:
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'axes.labelsize': 10,
        'axes.titlesize': 12,
        'xtick.labelsize': 8,
        'ytick.labelsize': 10,
        'legend.fontsize': 8,
        'figure.figsize': (9.0, 2.5)
    })

fig, ax = plt.subplots(1, 1, figsize=(9.0, 2.5))

# --- Plot: Grouped Stacked Distribution (Flipped) ---
bar_width = 0.12 
n_bars_per_group = n_cat # 7 bars per LLM group
group_separation = 1.0 
total_width_per_group = bar_width * n_bars_per_group

COLOR_HARM_BIN = "#E7951A"       
COLOR_NEUTRAL_LOW_BIN = "#6590E0" 
COLOR_SEVERE_HATCH = '#A5002A' 


# 1. Iterate over LLMs (main groups) in the new order
for i, llm in enumerate(llm_names):
    # Filter and sort by category for consistent bar order within the group
    df_llm = df[df['LLM'] == llm].sort_values(by='Category').reset_index(drop=True)
    
    # Calculate base x-position for the LLM group center
    base_x = i * group_separation
    
    # Calculate the starting position for the first bar in the group
    start_x = base_x - (total_width_per_group / 2) + (bar_width / 2)

    # Add LLM Name Label on Top 
    ax.text(
        base_x,
        1.05, 
        llm, # Full LLM name
        transform=ax.get_xaxis_transform(),
        ha='center',
        va='bottom',
        fontsize=9,
        weight='bold'
    )
    
    # 2. Iterate over Categories (bars within the group)
    for j, category in enumerate(categories):
        data_row = df_llm[df_llm['Category'] == category].iloc[0]
        x_pos = start_x + j * bar_width
        
        # Collect positions and labels for the new bottom axis
        all_x_positions.append(x_pos)
        all_x_labels.append(CRISIS_ABBREV_MAP[category])
        
        # --- Stacking code remains the same ---
        label_bin1 = '[1, 2.3]' if i == 0 and j == 0 else None
        ax.bar(x_pos, data_row['[1, 2.3]'], width=bar_width, label=label_bin1, color=COLOR_HARM_BIN)

        label_bin2 = '(2.3, 3.6]' if i == 0 and j == 0 else None
        ax.bar(x_pos, data_row['(2.3, 3.6]'], width=bar_width, bottom=data_row['[1, 2.3]'], label=label_bin2, color=COLOR_NEUTRAL_LOW_BIN)
        
        label_hatch = 'Score = 1' if i == 0 and j == 0 else None
        ax.bar(
            x_pos, data_row['1'], width=bar_width, label=label_hatch, 
            hatch='//////', fill=False, edgecolor=COLOR_SEVERE_HATCH, linewidth=0.8
        )


# --- 3. Set X-axis Ticks and Labels (The crisis abbreviations) ---
ax.set_xticks(all_x_positions)
ax.set_xticklabels(all_x_labels, rotation=90, ha='center', fontsize=7.5) 

# Remove ticks from both top and bottom axis
ax.tick_params(axis='x', which='major', length=0) 
ax.tick_params(axis='x', which='minor', length=0) 
ax.tick_params(axis='y', which='both', right=False)
ax.tick_params(axis='x', which='both', top=False) 

# Add vertical separator lines between LLM groups
llm_x_centers = np.arange(n_llm) * group_separation
separator_positions = llm_x_centers[:-1] + group_separation / 2 
for pos in separator_positions:
    ax.axvline(x=pos, color='grey', linestyle='--', linewidth=0.8, alpha=0.7)

# --- 4. Add Legends and Titles ---
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_ylim(0, 45)

# 4.1. Score Bin Legend (Moved to Top Left)
handles, labels = ax.get_legend_handles_labels()
bin_legend_handles = handles[:3]
bin_legend_labels = labels[:3]

# Reorder the Legend (Score=1 first)
order = [2, 0, 1]
bin_legend_handles = [bin_legend_handles[i] for i in order]
bin_legend_labels = [bin_legend_labels[i] for i in order]

legend1 = ax.legend(
    bin_legend_handles, 
    bin_legend_labels, 
    loc='upper right', # Changed to upper left
    bbox_to_anchor=(1., 0.9), # Aligned to the left edge
    ncol=3, frameon=True, fontsize=7, edgecolor='none'
)
ax.add_artist(legend1)

# 4.2. Category Abbreviation Legend (Text box - Moved to Top Right)
category_map_labels = [f"$\\bf{{{CRISIS_ABBREV_MAP[cat]}}}$: {cat}" for cat in categories]
category_legend_text = " - ".join(category_map_labels)

ax.text(
    0.055,
    0.96, # Positioned at the top
    category_legend_text,
    transform=ax.transAxes,
    fontsize=7,
    va='top',
    ha='left', # Aligned text to the right
    bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3', alpha=1)
)

# Adjust X-axis limits
ax.set_xlim(llm_x_centers[0] - group_separation/2, llm_x_centers[-1] + group_separation/2)

plt.tight_layout()
plt.savefig('results-llm-per-model-low.png', dpi=300)
#also pdf
plt.savefig('results-llm-per-model-low.pdf', dpi=300, format='pdf', bbox_inches='tight', pad_inches=0.1)
plt.close()