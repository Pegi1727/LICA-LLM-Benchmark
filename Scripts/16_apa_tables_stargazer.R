# 16_apa_tables_stargazer.R
library(stargazer)

df <- read.csv("data/raw/lica_raw_score_matrix.csv")
sink("tables/r_table_stargazer.tex")
stargazer(df[, -1], type = "latex", title = "Summary Statistics of Benchmark Evaluations", label = "tab:ratings")
sink()
cat("[R INFO] Stargazer APA table generated in tables/r_table_stargazer.tex
")
