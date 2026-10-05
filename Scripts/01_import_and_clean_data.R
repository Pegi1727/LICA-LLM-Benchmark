# 01_import_and_clean_data.R
library(tidyverse)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
cat(sprintf("[R INFO] Loaded %d essays across %d variables.
", nrow(df), ncol(df)))
stopifnot(all(df[, -1] >= 1 & df[, -1] <= 5))
cat("[R PASS] All scores strictly bounded between 1 and 5.
")
