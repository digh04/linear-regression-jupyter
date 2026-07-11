#!/usr/bin/env python
"""Command-line linear regression: scatter plot, fit, and evaluation."""

import sys

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    if len(sys.argv) != 4:
        print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
        sys.exit(1)

    filename = sys.argv[1]
    x_column = sys.argv[2]
    y_column = sys.argv[3]

    print("Loading File: {}".format(filename))
    print("Using {} for x and {} for y".format(x_column, y_column))

    dataset = pd.read_csv(filename)
    print(dataset)

    x = dataset[x_column]
    print(x)

    y = dataset[y_column]
    print(y)

    x_values = dataset[[x_column]]
    y_values = dataset[[y_column]]

    model = LinearRegression()
    model.fit(x_values, y_values)

    plt.scatter(x, y, color="red")
    plt.plot(x, model.predict(x_values), color="blue")
    plt.title("{} vs {}".format(y_column, x_column))
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig("linear_regression_python_output.png")

    r_squared = model.score(x_values, y_values)
    print("R-squared: {:.4f}".format(r_squared))


if __name__ == "__main__":
    main()
