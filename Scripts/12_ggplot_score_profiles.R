# 12_ggplot_score_profiles.R
library(ggplot2)
library(tidyr)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
long_df <- pivot_longer(df, cols = -id, names_to = c("Rater", "Dimension"), names_sep = "_(?=[A-Z]$)", values_to = "Score")

p <- ggplot(long_df, aes(x = Dimension, y = Score, fill = Rater)) +
  stat_summary(geom = "bar", fun = "mean", position = "dodge") +
  stat_summary(geom = "errorbar", fun.data = "mean_se", position = position_dodge(0.9), width = 0.2) +
  theme_classic() +
  labs(title = "Mean Dimension Scores by Evaluator (R ggplot2)")

ggsave("figures/r_figure2_profiles.png", p, width = 7, height = 4.5, dpi = 300)
