# first thing to do is to create the python environment using: 'python -m venv venv'
# activate the venv: 'venv\Scripts\activate'
# store packages install in another file (a txt file), 'pip freeze > packages.txt'
# to install the packages in another file, navigate to the file and run the command 'pip install -r packages.txt'
import numpy as np
import pandas as pd

#generate array of random numbers with 10 rows and five columns
data = np.random.randn(10, 5)


dataset_one = np.random.randint(low=-50, high=101, size=(10,5)) # numbers of array is from 50-100, with 10 rows and 5 columns

# manipulate the data provided in the data array
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
df_one = pd.DataFrame(dataset_one, columns=['col_1','col_2','col_3','col_4','col_5'])

print(df_one)
# print(df)
# print(df.mean())
