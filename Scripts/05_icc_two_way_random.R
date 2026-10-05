# 05_icc_two_way_random.R
library(irr)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
# Reshape for multi-rater ICC across all 20 units
long_scores <- data.frame(
  Human = unlist(df[, c("human_L", "human_I", "human_C", "human_A")]),
  GPT4o = unlist(df[, c("gpt_4o_L", "gpt_4o_I", "gpt_4o_C", "gpt_4o_A")]),
  Claude = unlist(df[, c("claude_3_5_sonnet_L", "claude_3_5_sonnet_I", "claude_3_5_sonnet_C", "claude_3_5_sonnet_A")]),
  Gemini = unlist(df[, c("gemini_1_5_pro_L", "gemini_1_5_pro_I", "gemini_1_5_pro_C", "gemini_1_5_pro_A")])
)

icc_res <- icc(long_scores, model = "twoway", type = "agreement", unit = "single")
print(icc_res)
