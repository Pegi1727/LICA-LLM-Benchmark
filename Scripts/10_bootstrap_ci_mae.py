# 10_bootstrap_ci_mae.py
import pandas as pd
import numpy as np

def bootstrap_mae(n_boot=1000, seed=42):
    np.random.seed(seed)
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    boot_res = []
    for m in models:
        diffs = []
        for d in dims:
            diffs.extend(np.abs(df[f"{m}_{d}"] - df[f"human_{d}"]))
        diffs = np.array(diffs)
        samples = [np.mean(np.random.choice(diffs, size=len(diffs), replace=True)) for _ in range(n_boot)]
        ci_low, ci_high = np.percentile(samples, [2.5, 97.5])
        boot_res.append({'Model': m, 'MAE': np.mean(diffs), '95%_CI_Low': ci_low, '95%_CI_High': ci_high})
    res_df = pd.DataFrame(boot_res)
    print("=== BOOTSTRAP 95% CI FOR MAE ===")
    print(res_df)
    res_df.to_csv("data/processed/bootstrap_ci_mae.csv", index=False)

if __name__ == '__main__':
    bootstrap_mae()
