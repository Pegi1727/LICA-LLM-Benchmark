# 08_paired_ttest_inference.py
import pandas as pd
from scipy import stats

def paired_ttests():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    out = []
    for m in models:
        h_vals = df[[f"human_{d}" for d in dims]].values.flatten()
        m_vals = df[[f"{m}_{d}" for d in dims]].values.flatten()
        t_stat, p_val = stats.ttest_rel(m_vals, h_vals)
        out.append({'Model': m, 't_stat': t_stat, 'p_val': p_val})
    out_df = pd.DataFrame(out)
    print("=== PAIRED T-TESTS (OVERALL) ===")
    print(out_df)
    out_df.to_csv("data/processed/paired_ttests.csv", index=False)

if __name__ == '__main__':
    paired_ttests()
