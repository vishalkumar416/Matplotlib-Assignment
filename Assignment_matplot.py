"""
Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of Matplotlib.
Matplotlib is a popular Python library used for data visualization. It enables the creation of static, interactive, and animated visualizations in Python. It is widely used because of its ease of use, flexibility, and ability to create a variety of visualizations.

Uses of Matplotlib:

Visualizing data patterns and distributions.
Enhancing data analysis with graphical representations.
Communicating insights effectively through charts and graphs.
Five plots using the Pyplot module:

Line plot
Scatter plot
Bar plot
Histogram
Box plot
"""

"""
Q2: What is a scatter plot?
A scatter plot is used to visualize the relationship between two numerical variables. It displays points on a 2D plane where the x and y coordinates represent the values of the variables.
"""
# code
import numpy as np
import matplotlib.pyplot as plt

# Data generation
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

# Scatter plot
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

"""
Q3: Why is the subplot() function used?
The subplot() function is used to create multiple plots in a single figure, enabling comparison between different visualizations.
"""
# code
# Data
x = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])
y2 = np.array([50, 20, 40, 20, 60, 70])
y3 = np.array([10, 20, 30, 40, 50, 60])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title('Line 1')

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title('Line 2')

plt.subplot(2, 2, 3)
plt.plot(x, y3)
plt.title('Line 3')

plt.subplot(2, 2, 4)
plt.plot(x, y4)
plt.title('Line 4')

plt.tight_layout()
plt.show()

"""
Q4: What is a bar plot? Why is it used?
A bar plot represents data with rectangular bars where the height (or length) of the bar is proportional to the data value. It is commonly used for comparing categories.
"""
# code
# Data
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Vertical bar plot
plt.bar(company, profit)
plt.title('Company Profit - Vertical Bar Plot')
plt.xlabel('Company')
plt.ylabel('Profit')
plt.show()

# Horizontal bar plot
plt.barh(company, profit)
plt.title('Company Profit - Horizontal Bar Plot')
plt.xlabel('Profit')
plt.ylabel('Company')
plt.show()

"""
Q5: What is a box plot? Why is it used?
A box plot is a graphical representation of the distribution of a dataset. It shows the median, quartiles, and potential outliers.
"""
# code
# Data
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

# Box plot
plt.boxplot([box1, box2], labels=['Box 1', 'Box 2'])
plt.title('Box Plot')
plt.ylabel('Values')
plt.show()

