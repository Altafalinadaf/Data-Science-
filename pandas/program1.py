import pandas as pd

# reading the data 
df=pd.read_csv("C:\\Users\\altaf\\Downloads\\house-prices.csv")

print(df)

# counting the missing values 
print("couting the missing values \n")
count = df.isnull().sum()
print(count)

# print("after counting filling the missing values ")
# df=df.fillna(0)
# print(df)

print("droping rows with any missing values")
df_cleaned = df.dropna()  # Drops rows with any missing value
print(df_cleaned)

# droping To drop only rows where all values are missing 
print("dropping only rows where all values are missed")
df_cleaned = df.dropna(how='all')
print(df_cleaned)

df = df.copy()
# Fill with Mean (for numerical data)
print("filling Price coulum with mean strategies")

df["Price"] = df["Price"].fillna(df["Price"].mean())
print(df)

print("filling Bedrooms column with meduim strategies")
df['Bedrooms']= df['Bedrooms'].fillna(df["Bedrooms"].median())
