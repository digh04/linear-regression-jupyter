#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using python to model Salary based on Years of Experience.

# This notebook is calculating Mean Squared Error (MSE), fitted line slope, fitted line intercept, and correlation coefficient using python.

# MSE allows for the comparison of the real data against predictions made by the model. The fit of the model is inferior because of the large MSE of 17523844.08. Note how the squaring in y squared units from the equation MSE = (1/n) * Σ (yᵢ - ŷᵢ)² drives attention toward bigger MSE values. n represents the observation number, yᵢ represents the real value, and ŷᵢ represents the predicted value made by the model.

# The slope is 8285.29, which represents the quantity by which the line increases by y compared against a singular x unit increase.

# The intercept is 29203.52 at x = 0, which represents a constant, base y value.

# The correlation value is 0.89, which represents a sizeable, positive relationship.

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


# In[7]:


dataset = pd.read_csv("regression_data.csv")


# In[8]:


dataset


# In[9]:


x= dataset["YearsExperience"]
x


# In[10]:


y= dataset["Salary"]
y


# In[15]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

# Data
x = dataset["YearsExperience"]
y = dataset["Salary"]

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)
print(f"Slope: = {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"r: {r_value:.2f}")
print(f"MSE: {mse:.2f}")

# Plot
plt.scatter(x, y, color="red")
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(1.5, max(y) - 1,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()