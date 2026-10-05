# 12_generate_figure2_barchart.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_barchart():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    records = []
    dims = ['L', 'I', 'C', 'A']
    raters = ['human', 'gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    for _, row in df.iterrows():
        for d in dims:
            for r in raters:
                records.append({'Essay': row['id'], 'Dimension': d, 'Rater': r, 'Score': row[f"{r}_{d}"]})
    long_df = pd.DataFrame(records)
    plt.figure(figsize=(8, 5))
    sns.barplot(data=long_df, x='Dimension', y='Score', hue='Rater', palette='tab10', errorbar='se')
    plt.title("Figure 2: Mean Dimension Scores by Rater", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("figures/Figure2_Dimension_Comparison.png", dpi=300)
    print("[INFO] Figure 2 saved.")

if __name__ == '__main__':
    plot_barchart()
