#!/usr/bin/env python
"""Command-line linear regression: fit, diagnostics, annotated plot, and PNG export."""

import sys

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


def main():
    if len(sys.argv) != 4:
        print("Usage: python linear_model.py <filename> <x_column> <y_column>")
        sys.exit(1)

    filename = sys.argv[1]
    x_column = sys.argv[2]
    y_column = sys.argv[3]

    print("Loading File: {}".format(filename))
    print("Using {} for x and {} for y".format(x_column, y_column))

    dataset = pd.read_csv(filename)
    x = dataset[x_column]
    y = dataset[y_column]

    slope, intercept, r_value, _p_value, _std_err = linregress(x, y)
    y_pred = slope * x + intercept
    mse = mean_squared_error(y, y_pred)

    print("Slope: {:.2f}".format(slope))
    print("Intercept: {:.2f}".format(intercept))
    print("Correlation coefficient (Pearson's r): {:.2f}".format(r_value))
    print("Mean Squared Error (MSE): {:.2f}".format(mse))

    plt.scatter(x, y, color="red", label="Observed data")
    plt.plot(x, y_pred, color="blue", label="Fitted line")
    plt.text(
        x.min() + 0.1,
        y.max() * 0.92,
        "Equation: y = {:.2f}x + {:.2f}\nCorrelation coefficient (r): {:.2f}".format(
            slope, intercept, r_value
        ),
        fontsize=10,
        bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "gray"},
    )
    plt.title("{} vs {}".format(y_column, x_column))
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend()
    plt.tight_layout()
    plt.savefig("regression_plot_python.png")
    print("Plot saved to regression_plot_python.png")


if __name__ == "__main__":
    main()
