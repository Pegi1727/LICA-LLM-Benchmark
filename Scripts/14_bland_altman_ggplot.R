# 14_bland_altman_ggplot.R
library(ggplot2)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
h_all <- unlist(df[, paste0("human_", c("L", "I", "C", "A"))])
g_all <- unlist(df[, paste0("gemini_1_5_pro_", c("L", "I", "C", "A"))])

ba_df <- data.frame(Mean = (h_all + g_all)/2, Diff = g_all - h_all)
mb <- mean(ba_df$Diff)
sd_d <- sd(ba_df$Diff)

p <- ggplot(ba_df, aes(x = Mean, y = Diff)) +
  geom_point(size = 3, alpha = 0.7, color = "navy") +
  geom_hline(yintercept = mb, color = "red", linetype = "solid") +
  geom_hline(yintercept = mb + 1.96*sd_d, color = "gray40", linetype = "dashed") +
  geom_hline(yintercept = mb - 1.96*sd_d, color = "gray40", linetype = "dashed") +
  theme_minimal() +
  labs(title = "Bland-Altman Plot: Gemini 1.5 Pro vs Human", y = "Difference (Gemini - Human)", x = "Mean Rating")

ggsave("figures/r_bland_altman_gemini.png", p, width = 6, height = 4.5, dpi = 300)
