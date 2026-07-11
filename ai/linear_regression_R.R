args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_R.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

cat("Loading File:", filename, "\n")
cat("Using", x_col, "for x and", y_col, "for y\n")

data <- read.csv(filename)
print(data)

formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

library(ggplot2)
plot <- ggplot(data, aes(x = .data[[x_col]], y = .data[[y_col]])) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue", se = FALSE) +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot, width = 8, height = 6)

print(summary(model))
