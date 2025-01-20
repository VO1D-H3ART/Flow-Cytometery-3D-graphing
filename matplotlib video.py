import numpy as np #generates data
import  matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d') # this makes an axis
##ax.scatter(1, 2, 3) #this makes a single point at the coordinates (1,2,3)

x_data = np.random.randint(0, 100, 500)
y_data = np.random.randint(0, 100, 500)
z_data = np.random.randint(0, 100, 500)

ax.scatter(x_data, y_data, z_data, marker="v") #this makes a scatter plot of the data

##this is the labels for the axis
ax.set_title('Random Data')
ax.set_xlabel('X Axis (cm)')
ax.set_ylabel('Y Axis (seconds)')
ax.set_zlabel('Z Axis (yes)')

plt.show() #this shows the plot