import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("telescope_data.csv")
df= df.drop(columns=["Unnamed: 0"])
df["class"]=(df["class"]== "g").astype(int)

x = df[df.columns[:-1]]
y = df[df.columns[-1]]

scaler=StandardScaler()
x = scaler.fit_transform(x)

x_train, x_temp, y_train,y_temp= train_test_split(x,y, test_size=0.4,random_state=0)
x_test, x_validate, y_test, y_validate= train_test_split(x_temp,y_temp, test_size=0.5,random_state=0)

model= tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation= 'relu'),
    tf.keras.layers.Dense(16, activation= 'relu'),
    tf.keras.layers.Dense(1, activation= 'sigmoid')
])

model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate=0.001),
              loss= tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy']
)

model.fit(x_train, y_train, batch_size=16,epochs=20, validation_data=(x_validate,y_validate) )

y_pred= model.predict(x_test)
y_pred_class= np.round(y_pred)

print(classification_report(y_pred_class,y_test))
