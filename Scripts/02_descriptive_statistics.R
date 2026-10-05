# 02_descriptive_statistics.R
library(psych)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
stats <- describe(df[, -1])[, c("n", "mean", "sd", "median", "min", "max", "skew", "kurtosis")]
print(round(stats, 2))
write.csv(stats, "data/processed/r_descriptive_statistics.csv")
