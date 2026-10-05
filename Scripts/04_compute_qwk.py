# 04_compute_qwk.py
import pandas as pd
from sklearn.metrics import cohen_kappa_score

def compute_qwk():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    results = []
    for m in models:
        for d in dims:
            h = df[f"human_{d}"]
            pred = df[f"{m}_{d}"]
            qwk = cohen_kappa_score(h, pred, weights='quadratic')
            results.append({'Model': m, 'Dimension': d, 'QWK': qwk})
    qwk_df = pd.DataFrame(results)
    print("=== QUADRATIC WEIGHTED KAPPA (QWK) ===")
    print(qwk_df)
    qwk_df.to_csv("data/processed/qwk_summary.csv", index=False)

if __name__ == '__main__':
    compute_qwk()
