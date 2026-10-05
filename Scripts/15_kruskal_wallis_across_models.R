# 15_kruskal_wallis_across_models.R
df <- read.csv("data/raw/lica_raw_score_matrix.csv")

scores <- c(
  unlist(df[, paste0("gpt_4o_", c("L", "I", "C", "A"))]),
  unlist(df[, paste0("claude_3_5_sonnet_", c("L", "I", "C", "A"))]),
  unlist(df[, paste0("gemini_1_5_pro_", c("L", "I", "C", "A"))])
)
groups <- rep(c("GPT4o", "Claude", "Gemini"), each = 20)

kw_test <- kruskal.test(scores ~ groups)
print(kw_test)
