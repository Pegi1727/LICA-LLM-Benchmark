# 03_compute_mae_per_dimension.R
library(tidyverse)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
models <- c("gpt_4o", "claude_3_5_sonnet", "gemini_1_5_pro")
dims <- c("L", "I", "C", "A")

res <- expand.grid(Model = models, Dimension = dims, stringsAsFactors = FALSE) %>%
  rowwise() %>%
  mutate(MAE = mean(abs(df[[paste0(Model, "_", Dimension)]] - df[[paste0("human_", Dimension)]])))

print(res)
write.csv(res, "data/processed/r_mae_summary.csv", row.names = FALSE)
