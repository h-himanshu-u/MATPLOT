
from matplotlib import pyplot as plt
import numpy as np

x = np.random.normal(500,10,1000)  #  loc,standard deviation,size(no of elements)

plt.hist(x, color = "red" )
plt.title("random histogram")

plt.show()