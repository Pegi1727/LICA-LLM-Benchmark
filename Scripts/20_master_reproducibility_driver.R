# 20_master_reproducibility_driver.R
# Master driver script for the complete R statistical suite

scripts <- c(
  "01_import_and_clean_data.R",
  "02_descriptive_statistics.R",
  "03_compute_mae_per_dimension.R",
  "04_quadratic_weighted_kappa.R",
  "05_icc_two_way_random.R",
  "06_fleiss_kappa_consensus.R",
  "07_bland_altman_analysis.R",
  "08_paired_ttest_eval.R",
  "09_wilcoxon_signed_rank_exact.R",
  "10_bootstrap_resampling_mae.R"
)

cat("===================================================
")
cat("Starting R Reproducibility Suite Execution
")
cat("===================================================
")

for (s in scripts) {
  cat(sprintf("Executing %s...
", s))
  tryCatch({
    source(file.path("scripts/r", s))
    cat(sprintf("[SUCCESS] %s completed.
", s))
  }, error = function(e) {
    cat(sprintf("[ERROR] in %s: %s
", s, conditionMessage(e)))
  })
}

cat("===================================================
")
cat("R Pipeline Execution Finished.
")
cat("===================================================
")
