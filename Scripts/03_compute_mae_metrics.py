# 03_compute_mae_metrics.py
import pandas as pd
import numpy as np

def compute_mae():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    res = []
    for m in models:
        for d in dims:
            mae = np.mean(np.abs(df[f"{m}_{d}"] - df[f"human_{d}"]))
            res.append({'Model': m, 'Dimension': d, 'MAE': mae})
    res_df = pd.DataFrame(res)
    print("=== CRITERION-SPECIFIC MAE ===")
    print(res_df)
    res_df.to_csv("data/processed/mae_summary.csv", index=False)

if __name__ == '__main__':
    compute_mae()
