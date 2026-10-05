# 15_bland_altman_plots.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_ba_plots():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = [('gpt_4o', 'GPT-4o'), ('claude_3_5_sonnet', 'Claude 3.5'), ('gemini_1_5_pro', 'Gemini 1.5')]
    dims = ['L', 'I', 'C', 'A']
    for m_col, m_label in models:
        means = []
        diffs = []
        for d in dims:
            h = df[f"human_{d}"]
            p = df[f"{m_col}_{d}"]
            means.extend((h + p) / 2.0)
            diffs.extend(p - h)
        m_bias = np.mean(diffs)
        sd = np.std(diffs, ddof=1)
        plt.figure(figsize=(6, 4))
        plt.scatter(means, diffs, alpha=0.7, color='darkblue')
        plt.axhline(m_bias, color='red', linestyle='-', label=f"Mean Bias: {m_bias:.2f}")
        plt.axhline(m_bias + 1.96*sd, color='gray', linestyle='--', label=f"+1.96 SD: {m_bias+1.96*sd:.2f}")
        plt.axhline(m_bias - 1.96*sd, color='gray', linestyle='--', label=f"-1.96 SD: {m_bias-1.96*sd:.2f}")
        plt.title(f"Bland-Altman: {m_label} vs Human", fontweight='bold')
        plt.xlabel("Mean Score")
        plt.ylabel("Difference (Model - Human)")
        plt.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(f"figures/bland_altman_{m_col}.png", dpi=300)
        plt.close()
    print("[INFO] Bland-Altman plots generated.")

if __name__ == '__main__':
    generate_ba_plots()
