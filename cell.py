import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

df= pd.read_csv("student-mat.csv") 
df= df.drop(columns=["school", "address", "Mjob", "Fjob", "reason", "guardian", "traveltime", "studytime", "absences", "G1","G2"])
df['sex']=(df["sex"]== 'M').astype(int)
df['famsize']= (df["famsize"]== "GT3").astype(int)
df["Pstatus"]= (df["Pstatus"]== 'T').astype(int)
df[["schoolsup","famsup","paid","activities","nursery", "higher","internet","romantic"]]= (df[["schoolsup","famsup","paid","activities","nursery", "higher","internet","romantic"]]== "yes").astype(int)
df['failures']= np.log(df["failures"] + 1)
df['Dalc']= np.log(df["Dalc"]+ 1)

def grade(score):
    if score >= 10:
        return 1
    else:
        return 0
df['G3']= df["G3"].apply(grade)

train, test, validate = np.split(df.sample(frac= 1), [int(0.8 * len(df)), int(0.9 * len(df))])

def scale_data(dataset, oversample= False):
    x = dataset[dataset.columns[:-1]]
    y= dataset[dataset.columns[-1]]

    scaler= StandardScaler()
    x= scaler.fit_transform(x)

    if oversample:
        ros= RandomOverSampler()
        x,y = ros.fit_resample(x,y)

    return x,y

x_train, y_train= scale_data(train, oversample=True)
x_test, y_test= scale_data(test)
x_validate, y_validate= scale_data(validate)



model= tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation= 'relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation= 'relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation= 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation= 'sigmoid')
])

model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate= 0.001),
              loss= 'binary_crossentropy',
              metrics= ['accuracy']
)

early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model.fit( x_train,y_train, batch_size= 20, epochs= 20, validation_data= (x_validate,y_validate)) 
y_pred= model.predict(x_test)
y_pred_class= np.round(y_pred).astype(int)

print(classification_report(y_test,y_pred_class))



