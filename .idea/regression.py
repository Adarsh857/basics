# Importing libraries
# Importing data
# REading data
# Data engineering
# train test split
# model making
# Output(Visualisation)
# Evaluation and Optimization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read_csv() is used to read a CSV file. It is a of pandas library
dataset = pd.read_csv('Salary_Data.csv')
print(dataset)
dataset.head(10)
dataset.tail()
X = dataset.iloc[:,:1]
print(X)
y = dataset.iloc[:,1]
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)
x_train.head()
x_test.head()
y_train.head()
y_test.head()
from sklearn.linear_model import LinearRegression

obj = LinearRegression()

obj.fit(x_train,y_train)
y_pred = obj.predict([[6.0]])

print(y_pred)
plt.scatter(x_train,y_train,color = 'black')
plt.plot(x_train,obj.predict(x_train),color = 'red')
plt.title('Experience vs Salary(Training) ')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()