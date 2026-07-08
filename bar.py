

from matplotlib import pyplot as plt
import numpy as np


x = np.array([4,8,7,5,5])
y = np.array([4,5,3,8,5])
plt.subplot(1,2,1)
plt.bar(x,y,color = "red")

plt.title("bar plot 2",loc = "left")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

x1 = np.array([1,5,4,5,7,4,6,3,1])
y1 = np.array([6,5,9,7,4,4,5,5,3])
plt.subplot(1,2,2)
plt.bar(x1,y1,color = "green")

plt.title("bar plot 2",loc = "left")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.show()