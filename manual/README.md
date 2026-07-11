# **Assignment 2 README.md**
## The purpose of the assignment is to create a succinct data analysis. The dataset regression_data.csv is read to make a scatter plot, fit a linear model, and overlay a regression line using Python and R.

## Tools/libraries used include:
   1. Jupyter notebook in both Python and R
   2. Linux
   3. GitHub
   4. regression_data.csv
### *Python:*
   5. pandas
   6. matplotlib
   7. LinearRegression
   8. sys
### *R:*
   9. commandArgs()
   10. ggplot2

## Part I
1. Create a Python and R notebook. Start each with a Markdown cell.
2. Import pandas and pd.read.csv for Python. read.csv for R.
3. Import matplotlib and plt.scatter() for Python. plot() for R.
4. Import LinearRegression and model.fit for Python. lm for R.
5. plt.plot for Python. install.packages("ggplot2") and ggplot() for R.
6. model.score() for Python. summary(model) for R.
7. Save and export both notebooks as .html. Save all in manual.

## Part II
1. Export both notebooks as executable script. Save in manual.
2. Edit both scripts.
### *Python:*
filename = sys.argv[1]
x_column = sys.argv[2]
y_column = sys.argv[3]

print("Loading File: {}".format(filename))
print("Using {} for x and {} for y".format(x_column,y_column))

dataset = pd.read_csv(filename)
print(dataset)

x= dataset[x_column]
print(x)

y= dataset[y_column]
print(y)

plt.scatter(x, y, color="red")
plt.title(f'{y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.savefig("linear_regression_python_output.png")
### *R:*
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript regression_R.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot)

3. Run both scripts.
### *Python:*
python regression_python.py regression_data.csv YearsExperience Salary
### *R:*
Rscript regression_R.r regression_data.csv YearsExperience Salary

4. Save all in manual.