# 11_generate_figure1_heatmap.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap():
    df = pd.read_csv("data/processed/mae_summary.csv")
    pivot = df.pivot(index='Model', columns='Dimension', values='MAE')
    plt.figure(figsize=(7, 4.5))
    sns.heatmap(pivot, annot=True, cmap="YlOrRd", fmt=".2f", cbar_kws={'label': 'Mean Absolute Error'})
    plt.title("Figure 1: Criterion-Specific MAE Heatmap", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig("figures/Figure1_MAE_Heatmap.png", dpi=300)
    print("[INFO] Figure 1 saved.")

if __name__ == '__main__':
    plot_heatmap()
