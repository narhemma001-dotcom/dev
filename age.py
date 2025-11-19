import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
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


model= StackingClassifier(
    estimators=[
        ('randomforest', RandomForestClassifier(random_state=42)),
        ('svm', SVC(probability=True, random_state=42)),
        ('knn', KNeighborsClassifier(n_neighbors=5))
    ],
    final_estimator= LogisticRegression(),
    cv= 5,
    n_jobs= -1,
    passthrough= True

)

model.fit(x_train,y_train)

y_pred= model.predict(x_test)
print(classification_report(y_test,y_pred))