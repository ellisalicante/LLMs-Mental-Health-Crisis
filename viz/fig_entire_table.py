import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

# 1. Manually transcribed data from the LaTeX table (Same data as before)
data = {
    'LLM': ['gpt-4o-mini'] * 7 + ['gpt-5-nano'] * 7 + ['llama-4-scout'] * 7 + ['deepseek-v3.2'] * 7 + ['grok-4-fast'] * 7,
    'Category': [
        'suicidal ideation', 'self-harm', 'anxiety crisis', 'violent thoughts', 'substance abuse', 'risk-taking behaviors', 'no crisis',
    ] * 5,
    'Mean Score': [
        3.673, 3.748, 4.567, 3.989, 3.984, 4.251, 4.955,
        4.931, 4.902, 4.984, 4.884, 4.941, 4.754, 4.938,
        4.333, 4.101, 4.664, 4.116, 4.336, 4.345, 4.961,
        4.842, 4.703, 4.979, 4.762, 4.747, 4.947, 4.965,
        4.480, 3.731, 4.930, 4.222, 4.622, 3.813, 4.951
    ],
    'Mean Std': [
        0.109, 0.129, 0.083, 0.030, 0.039, 0.211, 0.013,
        0.011, 0.014, 0.012, 0.052, 0.016, 0.017, 0.022,
        0.099, 0.099, 0.065, 0.067, 0.022, 0.108, 0.013,
        0.021, 0.047, 0.010, 0.090, 0.027, 0.033, 0.011,
        0.040, 0.066, 0.027, 0.082, 0.041, 0.083, 0.018
    ],
    '1': [
        1.14, 2.88, 0.00, 0.00, 0.00, 0.00, 0.11, 0.35, 1.20, 0.00, 0.00, 0.00, 0.00, 0.19, 2.19, 4.80, 0.00, 1.59, 0.00, 0.00, 0.08, 0.96, 1.92, 0.00, 0.00, 0.00, 0.00, 0.32, 6.40, 17.51, 0.00, 3.17, 0.43, 14.04, 0.38
    ],
    '[1, 2.3]': [
        2.72, 5.04, 0.00, 0.00, 0.00, 0.00, 0.41, 1.23, 1.68, 0.00, 0.00, 0.00, 5.26, 0.19, 3.95, 12.95, 0.00, 4.76, 0.00, 0.00, 0.08, 1.67, 3.12, 0.00, 0.00, 0.00, 0.00, 0.41, 9.39, 28.30, 0.00, 7.94, 0.43, 21.05, 0.41
    ],
    '(2.3, 3.6]': [
        26.93, 17.75, 1.69, 3.17, 7.79, 10.53, 0.16, 0.35, 0.72, 0.00, 0.00, 0.00, 1.75, 0.11, 5.88, 7.91, 1.13, 1.59, 0.43, 10.53, 0.22, 0.53, 1.68, 0.19, 0.00, 0.87, 0.00, 0.11, 2.28, 6.47, 0.19, 6.35, 0.43, 7.02, 0.00
    ],
    '(3.6, 5]': [
        70.35, 77.22, 98.31, 96.83, 92.21, 89.47, 99.43, 98.42, 97.60, 100.00, 100.00, 100.00, 92.98, 99.70, 90.18, 79.14, 98.87, 93.65, 99.57, 89.47, 99.70, 97.81, 95.20, 99.81, 100.00, 99.13, 100.00, 99.49, 88.33, 65.23, 99.81, 85.71, 99.13, 71.93, 99.59
    ]
}

df = pd.DataFrame(data)

# --- Configuration ---
METRIC_COLUMNS = ['Mean Score', 'Mean Std', '1', '[1, 2.3]', '(2.3, 3.6]', '(3.6, 5]']
METRIC_TITLES = {
    'Mean Score': 'Mean Score',
    'Mean Std': 'Mean Std',
    '1': 'Score = 1 (%)',
    '[1, 2.3]': '[1, 2.3] (%)',
    '(2.3, 3.6]': '(2.3, 3.6] (%)',
    '(3.6, 5]': '(3.6, 5] (%)'
}

NEW_CATEGORIES_ORDER = [
    'self-harm', 'suicidal ideation', 'risk-taking behaviors', 
    'violent thoughts', 'substance abuse', 'anxiety crisis', 'no crisis'
]
CATEGORY_ABBR = {
    'self-harm': 'Self-Harm', 
    'suicidal ideation': 'Suicidal Ideation', 
    'risk-taking behaviors': 'Risk-Taking', 
    'violent thoughts': 'Violent Thoughts', 
    'substance abuse': 'Substance Abuse', 
    'anxiety crisis': 'Anxiety Crisis', 
    'no crisis': 'No Crisis'
}


NEW_LLM_ORDER = [
    'grok-4-fast', 'gpt-4o-mini', 'llama-4-scout', 'gpt-5-nano', 'deepseek-v3.2'
]

# --- SET2 CMAP IMPLEMENTATION ---
cmap = plt.get_cmap('Set2')
LLM_COLORS = {
    'grok-4-fast': cmap(1), 
    'gpt-4o-mini': cmap(2), 
    'llama-4-scout': cmap(3), 
    'gpt-5-nano': cmap(0), 
    'deepseek-v3.2': cmap(4)
}
# --- END SET2 CMAP IMPLEMENTATION ---

# Data Sorting
cat_type = pd.CategoricalDtype(categories=NEW_CATEGORIES_ORDER, ordered=True)
df['Category'] = df['Category'].astype(cat_type)
llm_type = pd.CategoricalDtype(categories=NEW_LLM_ORDER, ordered=True)
df['LLM'] = df['LLM'].astype(llm_type)
df_sorted = df.sort_values(by=['LLM', 'Category']).reset_index(drop=True)

n_metrics = len(METRIC_COLUMNS) # Rows (6)
n_categories = len(NEW_CATEGORIES_ORDER) # Columns (7)
n_llms = len(NEW_LLM_ORDER)

# Define the highlight color and target metric indices
HIGHLIGHT_COLOR = '#FFDDDD' # Light reddish color
HIGHLIGHT_METRIC_INDICES = [
    METRIC_COLUMNS.index('1'), 
    METRIC_COLUMNS.index('[1, 2.3]')
]

# --- Plotting Setup ---
try:
    plt.style.use(['science', 'no-latex'])
    plt.rcParams.update({'font.family': 'serif', 'font.size': 10})
except:
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams.update({'font.family': 'serif', 'font.size': 10})

# Set up the figure (n_metrics rows, n_categories columns)
fig, axes = plt.subplots(
    n_metrics, n_categories, 
    figsize=(15, 11), 
    sharex=True, # X-axis is shared across all plots
    gridspec_kw={'hspace': 0.15, 'wspace': 0.05}
)

font_size_data_small = 6.5 # New size for Mean Score/Std
font_size_data_large = 8.5 # Size for percentages
font_size_titles = 10
font_size_tick_labels = 10 

# --- Bar Dimensions ---
bar_width = 0.8 
x_positions_base = np.arange(n_llms)
bar_center_offset = (n_llms - 1) / 2

# --- Main Plotting Loop (Rows = Metrics, Columns = Categories) ---
for i, metric in enumerate(METRIC_COLUMNS): # Rows (Metrics)
    for j, category in enumerate(NEW_CATEGORIES_ORDER): # Columns (Categories)
        ax = axes[i, j]
        
        # Add background highlight for specific rows
        if i in HIGHLIGHT_METRIC_INDICES:
            ax.patch.set_facecolor(HIGHLIGHT_COLOR)
            ax.patch.set_alpha(0.6) # Adjust transparency if needed

        # 1. Determine Y-axis properties (unique for each row/metric)
        metric_data = df_sorted[metric]
        y_min = 0 
        y_formatter = FormatStrFormatter('%.0f')
        
        if 'Mean Score' in metric:
            y_min = 3.5
            y_max = 5.1
            # Clean up Y-Axis Decimals: Mean Score to one decimal place
            y_formatter = FormatStrFormatter('%.1f') 
        elif 'Mean Std' in metric:
            y_max = metric_data.max() * 1.15
            # Clean up Y-Axis Decimals: Mean Std to two decimal places
            y_formatter = FormatStrFormatter('%.2f') 
        else: # Percentages
            y_max = 105.0 if '3.6, 5]' in metric else metric_data.max() * 1.25
            
        ax.set_ylim(y_min, y_max)

        # Filter data for the current subplot
        plot_data = df_sorted[df_sorted['Category'] == category].sort_values(by='LLM')
        
        # 2. Plot the bars
        for k, llm in enumerate(NEW_LLM_ORDER):
            value = plot_data[plot_data['LLM'] == llm][metric].iloc[0]
            
            ax.bar(x_positions_base[k] - bar_center_offset, value, 
                    width=bar_width, color=LLM_COLORS[llm], 
                    edgecolor='none', linewidth=0.5,
                    label=llm if i == 0 and j == 0 else None) 
            
            # 3. Add the number on top of the bar & set font size
            current_font_size = font_size_data_large
            if 'Mean Score' in metric:
                text_val = f'{value:.2f}'
                current_font_size = font_size_data_small # Smaller font for Mean Score
            elif 'Mean Std' in metric:
                text_val = f'{value:.3f}'
                current_font_size = font_size_data_small # Smaller font for Mean Std
            else: 
                text_val = f'{value:.0f}' if value >= 10.0 or '3.6, 5]' in metric else f'{value:.1f}'

            ax.text(
                x_positions_base[k] - bar_center_offset, value, text_val, 
                ha='center', va='bottom', fontsize=current_font_size, 
                rotation=0,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.1)
            )

        # --- Subplot Formatting ---
        
        # Set X-ticks to the center of each bar group
        ax.set_xticks(x_positions_base - bar_center_offset)
        ax.set_xlim(-bar_center_offset - bar_width, bar_center_offset + bar_width)
        
        # Remove LLM Names from X-Axis: only on the last row
        if i == n_metrics - 1:
            # Empty list for no x-labels
            ax.set_xticklabels([], rotation=45, ha='right', fontsize=font_size_tick_labels) 
        else: 
            ax.set_xticklabels([])
        
        # --- Remove ticks, just show line ---
        ax.tick_params(axis='x', which='both', length=0)
        ax.tick_params(axis='y', which='both', length=0)


        # Column Title (Category Label)
        if i == 0:
             # Category label is on the x-axis of the bottom row.
             ax.set_title(CATEGORY_ABBR[category], fontsize=font_size_titles, pad=5, weight='bold')
            
        # Row Title (Y-axis Label): only on the first column - NOW IT'S THE METRIC LABEL
        if j == 0:
            ax.set_ylabel(METRIC_TITLES[metric], fontsize=font_size_titles, rotation=90, ha='center', va='center', labelpad=10, weight='bold') # Full metric name
            ax.tick_params(axis='y', labelsize=font_size_tick_labels) 
            ax.yaxis.set_major_formatter(y_formatter) # Apply the dynamic formatter
        else: # Hide Y-ticks for all other columns
            ax.set_yticklabels([])
        
        # Aesthetics
        ax.grid(axis='y', linestyle=':', alpha=0.6)
        
        # --- Only bottom and left axes visible ---
        for spine in ['right', 'top']:
            ax.spines[spine].set_visible(False)
        
        # For non-first columns, hide left spine
        if j > 0:
            ax.spines['left'].set_visible(False)
        
        # Ensure bottom spine is visible for all
        ax.spines['bottom'].set_visible(True)
        # Ensure left spine is visible only for the first column
        ax.spines['left'].set_visible(j == 0)


# --- Final Legend (Moved to the bottom, no title, no frame) ---

# Create a single legend at the bottom center
handles, labels = axes[0, 0].get_legend_handles_labels()

fig.legend(
    handles, labels, 
    loc='lower center', bbox_to_anchor=(0.5, -0.01), ncol=n_llms, 
    frameon=False, title='', title_fontsize=0, fontsize=10 
)

# Adjust layout for the legend and rotated x-labels
plt.tight_layout(rect=[0, 0.05, 1, 0.98]) # Adjusted rect bottom for legend only
plt.savefig('figure-table.png', dpi=300)
plt.close()