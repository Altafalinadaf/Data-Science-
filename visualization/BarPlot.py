# A bar plot is useful for comparing categorical data across different categories.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Category':['A','B','C','D'],
        'Values':[10,20,30,40]}

df=pd.DataFrame(data)
print(df)

plt.title('Category VS Values')

sns.barplot(x='Category',y='Values',data=df,color='g')
plt.show()