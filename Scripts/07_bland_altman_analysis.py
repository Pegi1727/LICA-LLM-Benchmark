# 07_bland_altman_analysis.py
import pandas as pd
import numpy as np

def bland_altman():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    records = []
    for m in models:
        all_diffs = []
        for d in dims:
            diffs = df[f"{m}_{d}"] - df[f"human_{d}"]
            all_diffs.extend(diffs)
        mean_bias = np.mean(all_diffs)
        sd_diff = np.std(all_diffs, ddof=1)
        loa_lower = mean_bias - 1.96 * sd_diff
        loa_upper = mean_bias + 1.96 * sd_diff
        records.append({'Model': m, 'Mean_Bias': mean_bias, 'SD': sd_diff, 'LoA_Lower': loa_lower, 'LoA_Upper': loa_upper})
    ba_df = pd.DataFrame(records)
    print("=== BLAND-ALTMAN SUMMARY ===")
    print(ba_df)
    ba_df.to_csv("data/processed/bland_altman_metrics.csv", index=False)

if __name__ == '__main__':
    bland_altman()
