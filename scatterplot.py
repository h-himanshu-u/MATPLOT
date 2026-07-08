
from matplotlib import pyplot as plt
import numpy as np


x = np.array([3,6,4,8,7,5,5])
y = np.array([1,6,4,5,3,8,5])
plt.scatter(x,y,color = "red")

x1 = np.array([5,7,4,6,3,1])
y1 = np.array([7,4,4,5,5,3])
plt.scatter(x1,y1,color = "green")

plt.title("scatter plot",loc = "left")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.show()