# 09_wilcoxon_signed_rank_exact.R
library(coin)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
models <- c("gpt_4o", "claude_3_5_sonnet", "gemini_1_5_pro")
h_all <- unlist(df[, c("human_L", "human_I", "human_C", "human_A")])

for (m in models) {
  m_all <- unlist(df[, paste0(m, "_", c("L", "I", "C", "A"))])
  if (all(m_all == h_all)) {
    cat(sprintf("[%s] Identical ratings (Exact match = 100%%).
", m))
  } else {
    diffs <- m_all - h_all
    w_res <- wilcox.test(diffs, exact = TRUE)
    cat(sprintf("[%s vs Human] Wilcoxon V = %.1f, p-value = %.4f
", m, w_res$statistic, w_res$p.value))
  }
}
