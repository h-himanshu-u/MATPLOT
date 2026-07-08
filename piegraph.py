

from matplotlib import pyplot as plt
import numpy as np

x = np.array([45,55,65,75,85,40,])
labels1 = ['A','B','C','D','E','F']
set = ['red','green','blue','yellow','orange','pink']

plt.pie(x,labels = labels1,colors = set,explode = (0.1,0,0,0,0,0),shadow = True,startangle = 90)


plt.legend()

plt.title("pie chart")

plt.show()