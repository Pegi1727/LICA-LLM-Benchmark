# 13_spider_radar_chart.R
library(fmsb)

data <- as.data.frame(matrix(c(0.643, 0.643, 0.540, 0.286), nrow = 1))
colnames(data) <- c("Ideas", "Cohesion", "Language", "Appropriateness")
data <- rbind(rep(1, 4), rep(0, 4), data)

png("figures/r_figure3_radar.png", width = 600, height = 600, res = 120)
radarchart(data, axistype = 1, pcol = "#0073C2FF", pfcol = scales::alpha("#0073C2FF", 0.3), plwd = 2,
           title = "Autonomous AI Consensus (Fleiss Kappa)")
dev.off()
