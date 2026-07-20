# README EDITS
## Demonstrates IPIR

### Cloning assignment_2 and creating assignment3 branch
1. Start by cloning the original assignment_2 repository with git clone
2. cd assignment_2
3. Create assignment3 as a new branch using git checkout -b
4. Use gedit to create an edited README.md and name it README EDITS using Markdown

### Editing assignment_2 Python and R Jupyter notebooks
1. Using previous coding from assignment_2 as the foundation, add to the manual and ai folders by adding more information
2. More information includes adding more details in the scatter plot, adding Mean Squared Error, correlation coefficient, fitted line slope, fitted line intercept, PNG
3. More scatter plot details include equation, correlation coefficient, fitted regression line
4. Elaborate upon these in the notebook files linear_model_python.ipynb and linear_model_r.ipynb
5. The script files linear_model.py and linear_model.R should be the source for the PNG regression_plot_python.png and regression_plot_r.png

### GitHub
1. After making changes, git add . and git commit -m "Assignment 3: Regression annotations, diagnostics, and plots"
2. git push origin assignment3 and go to assignment3 branch URL to select Compare & pull request
3. base should be main and compare should be assignment3
4. branch test for title, and type the following for description: This is my code for assignment 3.
5. Select Merge pull request, squash and merge, and branch test (#1) for the commit message for two commits in the main

### Tags
1. To add tags, start with git checkout main and follow with git pull
2. Now git tag assignment3-final and git push origin assignment3-final
3. Take note of the URL to the main before the edits, the branch assignment3, and the version of assignment3 with the tag known as assignment3-final on main
