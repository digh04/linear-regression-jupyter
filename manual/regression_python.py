#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python/R] to model Salary based on Years of Experience.

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import sys


# In[17]:

filename = sys.argv[1]
x_column = sys.argv[2]
y_column = sys.argv[3]

print("Loading File: {}".format(filename))
print("Using {} for x and {} for y".format(x_column,y_column))

dataset = pd.read_csv(filename)
print(dataset)

# In[18]:


dataset


# In[19]:


x= dataset[x_column]
print(x)


# In[20]:


y= dataset[y_column]
print(y)


# In[21]:


plt.scatter(x, y, color="red")
plt.title(f'{y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.savefig("linear_regression_python_output.png")


# In[22]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[23]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[24]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared

