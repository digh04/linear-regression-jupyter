# Assignment 2: Linear Regression in Python and R

This project performs a simple linear regression analysis on `regression_data.csv`, modeling **Salary** as a function of **YearsExperience**. The same workflow is implemented in Python and R as Jupyter notebooks and as command-line scripts.

## Dataset

The CSV file is read from:

```
../manual/regression_data.csv
```

Columns used in the examples:

| Column            | Role        |
|-------------------|-------------|
| `YearsExperience` | Predictor (x) |
| `Salary`          | Response (y)  |

## Environment

All work uses the **`7030_class_2`** conda environment.

```bash
conda activate 7030_class_2
```

### Python libraries

- pandas
- matplotlib
- scikit-learn (`LinearRegression`)

### R libraries

- ggplot2

Kernels configured for Jupyter:

- Python: `7030_class_2` — display name **Python (7030_class_2)**
- R: `ir_7030_class_2` — display name **R (7030_class_2)**

## Notebooks

| File | Description |
|------|-------------|
| `linear_regression_python.ipynb` | Python analysis with scatter plot, fitted line, and R² |
| `linear_regression_R.ipynb` | R analysis with ggplot2, fitted line, and `summary(model)` |

Each notebook:

1. Loads the CSV from `../manual/regression_data.csv`
2. Creates a scatter plot
3. Fits a linear model
4. Overlays the regression line
5. Evaluates the model (R² in Python; full summary in R)

HTML exports:

- `linear_regression_python.html`
- `linear_regression_R.html`

To regenerate HTML from the notebooks:

```bash
conda activate 7030_class_2
cd /users/PAS3421/digh04/assignment_2/ai
jupyter nbconvert --to html linear_regression_python.ipynb
jupyter nbconvert --to html linear_regression_R.ipynb
```

## Command-line scripts

Both scripts accept three arguments: `<filename> <x_column> <y_column>`.

### Python

```bash
python linear_regression_python.py ../manual/regression_data.csv YearsExperience Salary
```

- Prints the loaded data and column values
- Fits `LinearRegression` using the specified columns
- Saves **`linear_regression_python_output.png`** (red scatter, blue regression line)
- Prints R² to the terminal

### R

```bash
Rscript linear_regression_R.R ../manual/regression_data.csv YearsExperience Salary
```

- Prints the loaded data
- Fits `lm(y ~ x, data)` with the specified columns
- Saves **`linear_regression_r_output.png`** using ggplot2 (red points, blue regression line)
- Prints `summary(model)` to the terminal

## Output files

| File | Source |
|------|--------|
| `linear_regression_python_output.png` | Python script |
| `linear_regression_r_output.png` | R script |
| `linear_regression_python.html` | Python notebook export |
| `linear_regression_R.html` | R notebook export |

## Workflow summary

```
regression_data.csv
        │
        ├── linear_regression_python.ipynb  →  linear_regression_python.html
        ├── linear_regression_R.ipynb       →  linear_regression_R.html
        ├── linear_regression_python.py     →  linear_regression_python_output.png
        └── linear_regression_R.R           →  linear_regression_r_output.png
```

Both languages should report a similar R² (about 0.79 for this dataset with 10 observations).
