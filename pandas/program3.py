import pandas as pd 

# Map Bedroom numbers to descriptions
df=pd.read_csv("C:\\Users\\altaf\\Downloads\\house-prices.csv")
print(df)
bedroom_mapping = {1: "Studio", 2: "1 Bedroom", 3: "2 Bedrooms", 4: "3 Bedrooms"}
df['Bedrooms'] = df['Bedrooms'].map(bedroom_mapping)

print(df)
