import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.xlabel("x values")
plt.ylabel("y values")
plt.plot(x,y)
plt.show()