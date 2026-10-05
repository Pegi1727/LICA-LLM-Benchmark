# 16_cross_rater_correlation_matrix.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_matrix():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    dims = ['L', 'I', 'C', 'A']
    raters = ['human', 'gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    flat_data = {r: [] for r in raters}
    for r in raters:
        for d in dims:
            flat_data[r].extend(df[f"{r}_{d}"])
    corr_df = pd.DataFrame(flat_data).corr(method='spearman')
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr_df, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Spearman Rank Correlation Across Raters", fontweight='bold')
    plt.tight_layout()
    plt.savefig("figures/Spearman_Correlation_Matrix.png", dpi=300)
    corr_df.to_csv("data/processed/spearman_correlations.csv")
    print("[INFO] Correlation matrix saved.")

if __name__ == '__main__':
    correlation_matrix()
