# 06_compute_fleiss_kappa.py
import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

def compute_fleiss():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    res = {}
    for d in dims:
        sub = df[[f"{m}_{d}" for m in models]]
        # Build count matrix for ratings (categories 1 to 5)
        counts = np.zeros((len(df), 5))
        for _, row in sub.iterrows():
            for val in row:
                counts[_, int(val)-1] += 1
        res[d] = fleiss_kappa(counts)
    res_df = pd.DataFrame(list(res.items()), columns=['Dimension', 'Fleiss_Kappa'])
    print("=== AUTONOMOUS AI FLEISS KAPPA ===")
    print(res_df)
    res_df.to_csv("data/processed/fleiss_kappa_ai_only.csv", index=False)

if __name__ == '__main__':
    compute_fleiss()
