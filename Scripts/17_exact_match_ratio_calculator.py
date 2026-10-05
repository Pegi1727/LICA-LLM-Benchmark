# 17_exact_match_ratio_calculator.py
import pandas as pd

def calculate_exact_matches():
    df = pd.read_csv("data/raw/lica_raw_score_matrix.csv")
    models = ['gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    dims = ['L', 'I', 'C', 'A']
    res = []
    for m in models:
        matches = 0
        total = len(df) * len(dims)
        for d in dims:
            matches += (df[f"{m}_{d}"] == df[f"human_{d}"]).sum()
        res.append({'Model': m, 'Exact_Matches': matches, 'Total': total, 'Ratio': matches / total})
    out = pd.DataFrame(res)
    print("=== EXACT MATCH RATIOS ===")
    print(out)
    out.to_csv("data/processed/exact_match_ratios.csv", index=False)

if __name__ == '__main__':
    calculate_exact_matches()
