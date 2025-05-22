import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = np.random.randint(low=0, high=20, size=(4,4)) 
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

means = df.mean() # find the mean of each column

# create a bar chart with the x-axis as the column names and y-axis as the means of the column
# width specifies the thickness of the bar 
plt.bar(means.index, means, width=0.3, color='skyblue', edgecolor='black')

plt.title('Mean values of each column')
plt.xlabel('Columns')
plt.ylabel('Mean Value')
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.show()