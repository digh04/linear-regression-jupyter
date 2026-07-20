dataset <- read.csv("regression_data.csv")

library(ggplot2)

# Fit model
model <- lm(Salary ~ YearsExperience, data = dataset)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(dataset$YearsExperience, dataset$Salary)
pred <- predict(model)
mse <- mean((dataset$Salary - pred)^2)
cat(sprintf("Slope: %.2f\n", slope))
cat(sprintf("Intercept: %.2f\n", intercept))
cat(sprintf("r: %.2f\n", r))
cat(sprintf("MSE: %.2f\n", mse))

# Plot
ggplot(dataset, aes(x = YearsExperience, y = Salary)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 1.5, y = max(dataset$Salary) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "YearsExperience", y = "Salary") +
  theme_minimal()

ggsave("regression_plot_r.png")