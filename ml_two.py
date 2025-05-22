import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(low=-100, high=101, size=(7,5))
df = pd.DataFrame(data, columns=['A', 'B','C', 'D', 'E'])

plt.plot(df['A'], label='Column A', marker='o')
plt.title('Plot of column A')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()