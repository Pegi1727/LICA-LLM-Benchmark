# 18_latex_table_generator.py
import pandas as pd

def export_latex_tables():
    desc = pd.read_csv("data/processed/descriptive_statistics.csv")
    with open("tables/table1_descriptives.tex", "w") as f:
        f.write(desc.to_latex(index=False, float_format="%.2f", caption="Descriptive Statistics of Evaluation Scores", label="tab:desc"))
    print("[INFO] LaTeX Table 1 exported.")

if __name__ == '__main__':
    import os; os.makedirs("tables", exist_ok=True)
    export_latex_tables()
