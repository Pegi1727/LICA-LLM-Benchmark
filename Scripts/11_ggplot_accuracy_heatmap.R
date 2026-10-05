# 11_ggplot_accuracy_heatmap.R
library(ggplot2)

mae_df <- read.csv("data/processed/r_mae_summary.csv")
p <- ggplot(mae_df, aes(x = Dimension, y = Model, fill = MAE)) +
  geom_tile(color = "white") +
  geom_text(aes(label = sprintf("%.2f", MAE)), color = "black", fontface = "bold") +
  scale_fill_distiller(palette = "YlOrRd", direction = 1) +
  theme_minimal() +
  labs(title = "Criterion-Specific MAE Heatmap (R ggplot2)")

ggsave("figures/r_figure1_heatmap.png", p, width = 6, height = 4, dpi = 300)
