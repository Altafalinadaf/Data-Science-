# A histogram is used to show the distribution of numerical data by splitting it into bins.

import numpy as np
import matplotlib.pyplot as plt

# Sample data for histogram
data =np.random.randn(1000) # 1000 random values from a normal distribution 

# hostogram plot 
# plt.hist(data,bins=30,color='purple',edgecolor='black')
# plt.title("Histogram of Random data")
# plt.xlabel('Values')
# plt.ylabel('Frequency')

# plt.show()


# scatter plot
x = np.random.rand(50)  # 50 random values for x-axis
y = 2 * x + np.random.randn(50) * 0.1  # Linearly related data with some noise


plt.scatter(x, y, color='orange')
plt.title('Scatter Plot of x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

