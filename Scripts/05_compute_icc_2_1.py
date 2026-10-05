# 05_compute_icc_2_1.py
import pandas as pd
import pingouin as pg

def compute_icc():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    # Melt to long format for pingouin ICC
    rows = []
    for _, r in df.iterrows():
        for d in ['L', 'I', 'C', 'A']:
            target_id = f"{r['id']}_{d}"
            rows.append({'Target': target_id, 'Rater': 'Human', 'Score': r[f"human_{d}"]})
            rows.append({'Target': target_id, 'Rater': 'GPT-4o', 'Score': r[f"gpt_4o_{d}"]})
            rows.append({'Target': target_id, 'Rater': 'Claude', 'Score': r[f"claude_3_5_sonnet_{d}"]})
            rows.append({'Target': target_id, 'Rater': 'Gemini', 'Score': r[f"gemini_1_5_pro_{d}"]})
    long_df = pd.DataFrame(rows)
    icc = pg.intraclass_corr(data=long_df, targets='Target', raters='Rater', ratings='Score')
    print("=== INTRACLASS CORRELATION COEFFICIENTS ===")
    print(icc.set_index('Type'))
    icc.to_csv("data/processed/icc_summary.csv", index=False)

if __name__ == '__main__':
    compute_icc()
