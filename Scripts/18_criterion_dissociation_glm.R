# 18_criterion_dissociation_glm.R
library(tidyverse)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
# Logistic regression for probability of rater disagreement as a function of criterion
diff_data <- data.frame()
dims <- c("L", "I", "C", "A")

for (d in dims) {
  disagree <- (df[[paste0("claude_3_5_sonnet_", d)]] != df[[paste0("human_", d)]]) | 
              (df[[paste0("gemini_1_5_pro_", d)]] != df[[paste0("human_", d)]])
  diff_data <- rbind(diff_data, data.frame(Dimension = d, Disagree = as.integer(disagree)))
}

fit <- glm(Disagree ~ Dimension, data = diff_data, family = binomial)
summary(fit)
