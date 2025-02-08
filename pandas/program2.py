import pandas as pd


df=pd.read_csv("C:\\Users\\altaf\\Downloads\\house-prices.csv")
print(df)

# using apply()

# Apply a function to increase 'Price' by 10%
df['Price']=df['Price'].apply(lambda x:x*1.10)
print(df)


# Apply a function to convert 'SqFt' to square meters (1 SqFt = 0.092903 m²)
df['SqFt']=df['SqFt'].apply(lambda x:x*0.092903)

print(df)