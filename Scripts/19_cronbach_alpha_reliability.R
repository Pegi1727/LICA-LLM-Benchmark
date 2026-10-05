# 19_cronbach_alpha_reliability.R
library(psych)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
# Alpha for the 4 LICA dimensions evaluated by the human gold standard
human_sub <- df[, c("human_L", "human_I", "human_C", "human_A")]
alpha_res <- psych::alpha(human_sub)
cat(sprintf("Standardized Cronbach's Alpha: %.3f
", alpha_res$total$std.alpha))
