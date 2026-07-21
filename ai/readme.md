# Assignment 3: Linear Regression in Python and R

This project performs a linear regression analysis on `regression_data.csv`, modeling **Salary** as a function of **YearsExperience**. The same workflow is implemented in Python and R as Jupyter notebooks and as command-line scripts.

## Dataset

The CSV file is read from:

```
../manual/regression_data.csv
```

Columns used in the examples:

| Column            | Role          |
|-------------------|---------------|
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
- scipy (`linregress`)
- scikit-learn (`mean_squared_error`)

### R libraries

- ggplot2

Kernels configured for Jupyter:

- Python: `7030_class_2` — display name **Python (7030_class_2)**
- R: `ir_7030_class_2` — display name **R (7030_class_2)**

## Notebooks

| File | Description |
|------|-------------|
| `linear_model_python.ipynb` | Python analysis with slope, intercept, Pearson's r, MSE, and annotated plot |
| `linear_model_r.ipynb` | R analysis with the same diagnostics and annotated ggplot2 plot |

Each notebook:

1. Loads the CSV from `../manual/regression_data.csv`
2. Explains what slope, intercept, correlation, and MSE measure (markdown cells)
3. Fits a linear model (`Salary` vs `YearsExperience`)
4. Prints slope, intercept, Pearson's r, and MSE
5. Displays a scatter plot with the fitted regression line and a text annotation showing the equation and correlation

## Command-line scripts

Both scripts accept three arguments: `<filename> <x_column> <y_column>`.

### Python

```bash
python linear_model.py ../manual/regression_data.csv YearsExperience Salary
```

- Prints slope, intercept, correlation coefficient (Pearson's r), and MSE
- Saves **`regression_plot_python.png`** (red scatter, blue regression line, equation and r annotated)

### R

```bash
Rscript linear_model.R ../manual/regression_data.csv YearsExperience Salary
```

- Prints slope, intercept, correlation coefficient (Pearson's r), and MSE
- Saves **`regression_plot_r.png`** using ggplot2 (red points, blue regression line, equation and r annotated)

## Output files

| File | Source |
|------|--------|
| `regression_plot_python.png` | Python script |
| `regression_plot_r.png` | R script |

## Workflow summary

```
regression_data.csv (in manual/)
        │
        ├── linear_model_python.ipynb
        ├── linear_model_r.ipynb
        ├── linear_model.py     →  regression_plot_python.png
        └── linear_model.R      →  regression_plot_r.png
```

Both languages should report similar values for this dataset (about 8285 slope, 29204 intercept, 0.89 Pearson's r, and MSE near 1.75e7).
