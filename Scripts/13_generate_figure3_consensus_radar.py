# 13_generate_figure3_consensus_radar.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_radar():
    df = pd.read_csv("data/processed/fleiss_kappa_ai_only.csv")
    labels = df['Dimension'].tolist()
    stats = df['Fleiss_Kappa'].tolist()
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    stats += stats[:1]
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='#1f77b4', alpha=0.3)
    ax.plot(angles, stats, color='#1f77b4', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11, fontweight='bold')
    ax.set_title("Figure 3: Autonomous AI Fleiss' Kappa Consensus", pad=20, fontweight='bold')
    plt.tight_layout()
    plt.savefig("figures/Figure3_Consensus_Radar.png", dpi=300)
    print("[INFO] Figure 3 saved.")

if __name__ == '__main__':
    plot_radar()
