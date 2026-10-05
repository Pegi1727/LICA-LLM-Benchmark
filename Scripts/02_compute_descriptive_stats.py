# 02_compute_descriptive_stats.py
import pandas as pd

def compute_descriptives(filepath="data/raw/lica_raw_score_matrix.csv"):
    df = pd.read_csv(filepath)
    score_cols = [c for c in df.columns if c != 'id']
    desc = df[score_cols].describe().T[['mean', 'std', 'min', '50%', 'max']]
    desc.columns = ['Mean', 'SD', 'Min', 'Median', 'Max']
    print("=== DESCRIPTIVE STATISTICS ===")
    print(desc)
    desc.to_csv("data/processed/descriptive_statistics.csv")
    print("[INFO] Saved to descriptive_statistics.csv")

if __name__ == '__main__':
    compute_descriptives()
