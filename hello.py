import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
 
df= pd.read_csv("telescope_data.csv")
df= df.drop(columns=["Unnamed: 0"])
df["class"]= (df["class"] == "g").astype(int)

train, test, validate = np.split(df.sample(frac=1), [int(0.6 * len(df)), int(0.8 * len(df))])

def scale_data(dataset, oversample= False):
    x= dataset[dataset.columns[:-1]]
    y= dataset[dataset.columns[-1]]

    scaler= StandardScaler()
    x= scaler.fit_transform(x)
    
    if oversample:
        ros= RandomOverSampler()
        x,y = ros.fit_resample(x,y)

    return  x, y

x_train, y_train= scale_data(train, oversample=True)
x_test, y_test= scale_data(test)
x_validate, y_validate= scale_data(validate)

model= SVC()
model.fit(x_train,y_train)

y_pred= model.predict(x_test)

print(classification_report(y_pred,y_test))

