args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_model.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

cat("Loading File:", filename, "\n")
cat("Using", x_col, "for x and", y_col, "for y\n")

data <- read.csv(filename)
x <- data[[x_col]]
y <- data[[y_col]]

formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(x, y)
pred <- predict(model)
mse <- mean((y - pred)^2)

cat(sprintf("Slope: %.2f\n", slope))
cat(sprintf("Intercept: %.2f\n", intercept))
cat(sprintf("Correlation coefficient (Pearson's r): %.2f\n", r))
cat(sprintf("Mean Squared Error (MSE): %.2f\n", mse))

library(ggplot2)

plot <- ggplot(data, aes(x = .data[[x_col]], y = .data[[y_col]])) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue", se = FALSE) +
  annotate(
    "text",
    x = min(x) + 0.1,
    y = max(y) * 0.92,
    label = paste0(
      "Equation: y = ", round(slope, 2), "x + ", round(intercept, 2),
      "\nCorrelation coefficient (r): ", round(r, 2)
    ),
    hjust = 0,
    size = 3.5
  ) +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("regression_plot_r.png", plot, width = 8, height = 6)
cat("Plot saved to regression_plot_r.png\n")
