import pandas as pd
import matplotlib.pyplot as plt
# need to install this "pip install scikit-learn"
# used to split the dataset into training and testing sets.
from sklearn.model_selection import train_test_split

# used to create and train a linear regression model.
from sklearn.linear_model import LinearRegression

# used to evaluate the performance of the trained model.
from sklearn.metrics import mean_squared_error,r2_score


# loand the dataset
df = pd.read_csv("C:\\Users\\altaf\\Downloads\\house-prices.csv")

# just checking by priting whether data is loaded or not 
print(df)

X= df[['SqFt']] #Independent Variable (feature)
y =df[['Price']] #Dependent variable (target)

# Split the data into traning and testing sets (80% train, 20% test)
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=43)

# create a linear regression model 
model= LinearRegression()

# train the model using the train data 
model.fit(X_train,y_train)

# make predictions on test data
y_pred = model.predict(X_test)

mse= mean_squared_error(y_test,y_pred)







