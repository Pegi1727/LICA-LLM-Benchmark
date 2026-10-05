# 04_quadratic_weighted_kappa.R
library(vcd)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
models <- c("gpt_4o", "claude_3_5_sonnet", "gemini_1_5_pro")
dims <- c("L", "I", "C", "A")

results <- data.frame()
for (m in models) {
  for (d in dims) {
    tab <- table(factor(df[[paste0("human_", d)]], levels=1:5),
                 factor(df[[paste0(m, "_", d)]], levels=1:5))
    kw <- Kappa(tab, weights = "Fleiss-Cohen")
    results <- rbind(results, data.frame(Model=m, Dimension=d, QWK=kw$Weighted$value))
  }
}
print(results)
write.csv(results, "data/processed/r_qwk_summary.csv", row.names = FALSE)
