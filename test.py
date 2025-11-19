import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


df= pd.read_csv("test.csv")
df= df.drop(columns=['Date','Hour','Wind speed (m/s)','Visibility (10m)','Solar Radiation (MJ/m2)','Rainfall(mm)','Snowfall (cm)','Seasons','Holiday','Functioning Day'])

x= df[["Humidity(%)","Dew point temperature(ｰC)"]]
y= df["Temperature(ｰC)"]

x_train,x_temp,y_train,y_temp= train_test_split(x,y, test_size= 0.4)
x_test,x_validate,y_test,y_validate= train_test_split(x_temp,y_temp, test_size= 0.5)

model= LinearRegression()
model.fit(x_train,y_train)

y_pred= model.predict(x_test)
mse= mean_squared_error(y_test,y_pred)

# print(model.score(x_test,y_test))
# print(mse)
print(df.corr(method='pearson'))
print(df.skew())