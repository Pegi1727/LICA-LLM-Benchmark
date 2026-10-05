# 08_paired_ttest_eval.R
df <- read.csv("data/raw/lica_raw_score_matrix.csv")
models <- c("gpt_4o", "claude_3_5_sonnet", "gemini_1_5_pro")
h_all <- unlist(df[, c("human_L", "human_I", "human_C", "human_A")])

for (m in models) {
  m_all <- unlist(df[, paste0(m, "_", c("L", "I", "C", "A"))])
  t_res <- t.test(m_all, h_all, paired = TRUE)
  cat(sprintf("[%s vs Human] t = %.3f, p-value = %.4f
", m, t_res$statistic, t_res$p.value))
}
