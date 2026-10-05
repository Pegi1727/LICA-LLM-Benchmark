# 14_generate_figure4_deviation_spectrum.py
import pandas as pd
import matplotlib.pyplot as plt

def plot_deviation_spectrum():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    items = []
    for _, row in df.iterrows():
        for d in dims:
            items.append(f"{row['id']}-{d}")
    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True, sharey=True)
    for ax, m in zip(axes, models):
        deltas = []
        for _, row in df.iterrows():
            for d in dims:
                deltas.append(row[f"{m}_{d}"] - row[f"human_{d}"])
        ax.bar(items, deltas, color=['#2ca02c' if x==0 else ('#ff7f0e' if x>0 else '#1f77b4') for x in deltas])
        ax.axhline(0, color='black', linestyle='--')
        ax.set_title(f"Deviation Profile: {m}", loc='left', fontweight='bold')
    plt.tight_layout()
    plt.savefig("figures/Figure4_Calibration_Deviations.png", dpi=300)
    print("[INFO] Figure 4 saved.")

if __name__ == '__main__':
    plot_deviation_spectrum()
