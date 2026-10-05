# 20_reproducibility_pipeline_runner.py
import subprocess
import sys

def run_all():
    scripts = [
        "01_data_ingestion_validation.py",
        "02_compute_descriptive_stats.py",
        "03_compute_mae_metrics.py",
        "04_compute_qwk.py",
        "05_compute_icc_2_1.py",
        "06_compute_fleiss_kappa.py",
        "07_bland_altman_analysis.py",
        "08_paired_ttest_inference.py",
        "09_wilcoxon_signed_rank.py",
        "10_bootstrap_ci_mae.py",
        "17_exact_match_ratio_calculator.py"
    ]
    print("[START] Executing Full Python Reproducibility Pipeline...")
    for s in scripts:
        print(f"--> Running {s}")
        res = subprocess.run([sys.executable, f"scripts/py/{s}"], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"[FAIL] {s}: {res.stderr}")
        else:
            print(f"[OK] {s}")
    print("[COMPLETE] All pipeline scripts executed successfully.")

if __name__ == '__main__':
    run_all()
