
# A line plot is typically used to visualize continuous data and trends over time or other ordered variables.

import matplotlib.pyplot as plt
import pandas as pd

data = {'Months':['jan','feb','mar','apr','may','june'],
        'Sales':[120,300,600,20,145,543]}
df=pd.DataFrame(data)

print(df)

# line plot Exmaple 
plt.plot(df['Months'],df['Sales'],marker='o',color='b',label='Sales')

plt.title("Sales Trend over a month ")
plt.xlabel('Months')
plt.ylabel('Sales')

plt.legend()
plt.show()