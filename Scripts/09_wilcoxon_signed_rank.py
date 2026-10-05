# 09_wilcoxon_signed_rank.py
import pandas as pd
from scipy import stats

def wilcoxon_tests():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    out = []
    for m in models:
        h_vals = df[[f"human_{d}" for d in dims]].values.flatten()
        m_vals = df[[f"{m}_{d}" for d in dims]].values.flatten()
        # if identical, handle zero differences
        diff = m_vals - h_vals
        if (diff == 0).all():
            w_stat, p_val = 0.0, 1.0
        else:
            w_stat, p_val = stats.wilcoxon(diff[diff != 0], zero_method='wilcox')
        out.append({'Model': m, 'W_stat': w_stat, 'p_val': p_val})
    res_df = pd.DataFrame(out)
    print("=== WILCOXON SIGNED-RANK TESTS ===")
    print(res_df)
    res_df.to_csv("data/processed/wilcoxon_tests.csv", index=False)

if __name__ == '__main__':
    wilcoxon_tests()
