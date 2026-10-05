# 07_bland_altman_analysis.R
library(BlandAltmanLeh)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
h_all <- unlist(df[, c("human_L", "human_I", "human_C", "human_A")])
c_all <- unlist(df[, c("claude_3_5_sonnet_L", "claude_3_5_sonnet_I", "claude_3_5_sonnet_C", "claude_3_5_sonnet_A")])

ba <- bland.altman.stats(c_all, h_all)
cat(sprintf("Mean bias: %.3f | Upper LoA: %.3f | Lower LoA: %.3f
", ba$mean.diffs, ba$upper.limit, ba$lower.limit))
