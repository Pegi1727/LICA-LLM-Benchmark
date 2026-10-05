# 10_bootstrap_resampling_mae.R
library(boot)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
gem_diffs <- abs(unlist(df[, paste0("gemini_1_5_pro_", c("L", "I", "C", "A"))]) - 
                 unlist(df[, paste0("human_", c("L", "I", "C", "A"))]))

boot_fn <- function(d, indices) mean(d[indices])
b_out <- boot(gem_diffs, boot_fn, R = 2000)
b_ci <- boot.ci(b_out, type = "perc")
print(b_ci)
