import matplotlib.pyplot as plt
import numpy as np

arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([2,4,6,8,10])

plt.plot(arr_1, arr_2, label='Linear growth') # plot a graph with values of arr_1 on the x-axis and arr_2 on the y-axis
plt.title('Simple plot graph') # specify the title of the graph

# label the x and the y axis
plt.xlabel('X axis') 
plt.ylabel('Y label')

plt.legend() # Display the legend of the graph which shows the string in the label
plt.grid(True) # display grids

plt.show()