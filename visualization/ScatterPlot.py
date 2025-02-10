import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)  # 50 random values for x-axis
y = 2 * x + np.random.randn(50) * 0.1  # Linearly related data with some noise


plt.scatter(x, y, color='orange')
plt.title('Scatter Plot of x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()