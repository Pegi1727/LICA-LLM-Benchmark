# 01_data_ingestion_validation.py
import pandas as pd
import numpy as np

def validate_data(filepath="data/raw/lica_raw_score_matrix.csv"):
    df = pd.read_csv(filepath)
    print(f"[INFO] Loaded {len(df)} essays.")
    dims = ['L', 'I', 'C', 'A']
    raters = ['human', 'gpt_4o', 'claude_3_5_sonnet', 'gemini_1_5_pro']
    for r in raters:
        for d in dims:
            col = f"{r}_{d}"
            assert col in df.columns, f"Missing column {col}"
            assert df[col].between(1, 5).all(), f"Out of bounds in {col}"
    print("[PASS] Score matrix schema and bound constraints (1-5) strictly verified.")

if __name__ == '__main__':
    validate_data()
