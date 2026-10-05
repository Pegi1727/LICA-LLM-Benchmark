# 06_fleiss_kappa_consensus.R
library(irr)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
dims <- c("L", "I", "C", "A")

for (d in dims) {
  ratings <- df[, c(paste0("gpt_4o_", d), paste0("claude_3_5_sonnet_", d), paste0("gemini_1_5_pro_", d))]
  fk <- kappam.fleiss(ratings)
  cat(sprintf("Fleiss' Kappa for Dimension %s: %.3f (p = %.4f)
", d, fk$value, fk$p.value))
}
