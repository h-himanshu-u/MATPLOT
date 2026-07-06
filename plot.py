
import matplotlib.pyplot as plt
import numpy as np 


x = np.array([1,6,5,2,4,3])
y = np.array([6,2,8,10,2,2])
z = np.array([4,3,2,5,7,4])
plt.plot(x,color = "red",ls = "--",marker = "H", mec = "blue",mfc ="orange",ms ="9")
plt.plot(y,color = "green",ls = ":",marker = "o",mec = "brown",mfc ="red",ms = "10")
plt.plot(z,color = "pink",ls ="-." , marker = "*" , mec = "purple",mfc = "yellow",ms = "8")

fint = { "family" : "serif" , "color" : "blue" }

plt.title("line plot", fontdict = fint,loc = "center")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.grid(axis = "x")
plt.grid(axis = "y")
plt.grid(color = "grey",lw = "0.1")
plt.show()