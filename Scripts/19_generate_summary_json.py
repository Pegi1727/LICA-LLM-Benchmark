# 19_generate_summary_json.py
import pandas as pd
import json

def generate_json_summary():
    mae = pd.read_csv("data/processed/mae_summary.csv")
    qwk = pd.read_csv("data/processed/qwk_summary.csv")
    summary = {
        "benchmark_metadata": {"sample_size": 5, "dimensions": 4, "total_evals": 20},
        "models": ["gpt_4o", "claude_3_5_sonnet", "gemini_1_5_pro"],
        "overall_mae": mae.groupby('Model')['MAE'].mean().to_dict(),
        "mean_qwk": qwk.groupby('Model')['QWK'].mean().to_dict()
    }
    with open("data/processed/lica_benchmark_meta.json", "w") as f:
        json.dump(summary, f, indent=4)
    print("[INFO] JSON benchmark summary written.")

if __name__ == '__main__':
    generate_json_summary()
