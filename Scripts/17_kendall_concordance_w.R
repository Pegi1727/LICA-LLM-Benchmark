# 17_kendall_concordance_w.R
library(irr)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
# Evaluating W across all 4 raters for each of the 20 items
ratings_matrix <- cbind(
  unlist(df[, paste0("human_", c("L", "I", "C", "A"))]),
  unlist(df[, paste0("gpt_4o_", c("L", "I", "C", "A"))]),
  unlist(df[, paste0("claude_3_5_sonnet_", c("L", "I", "C", "A"))]),
  unlist(df[, paste0("gemini_1_5_pro_", c("L", "I", "C", "A"))])
)

w_res <- kendall(ratings_matrix, correct = TRUE)
print(w_res)
