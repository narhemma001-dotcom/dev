import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split


train_df= pd.read_csv("train.csv")
test_df= pd.read_csv("test.csv")

#filling age cos it is deficient
train_df["Age"]= train_df["Age"].fillna(train_df["Age"].mean())
train_df["Sex"]= (train_df["Sex"]== "male").astype(int)
train_df= train_df.drop(columns= ["Name","Cabin","Embarked","Ticket","Fare","PassengerId"])

#this is to check for skewness, out of the data this two were extrmely positively skewed
train_df["SibSp"]= np.log1p(train_df["SibSp"])
train_df["Parch"]= np.log1p(train_df["Parch"])

#separating data into features and column
x= train_df.drop(columns="Survived")
y= train_df["Survived"]

#filling age cos it is deficient
test_df["Age"]= test_df["Age"].fillna(train_df["Age"].mean())
test_df["Sex"]= (test_df["Sex"]== "male").astype(int)
test_df= test_df.drop(columns= ["Name","Cabin","Embarked","Ticket","Fare","PassengerId"])
test_df["SibSp"]= np.log1p(test_df["SibSp"])
test_df["Parch"]= np.log1p(test_df["Parch"])


x_train, x_validate, y_train, y_validate= train_test_split(x,y, test_size= 0.4, random_state= 42)

ros= RandomOverSampler()
x_train,y_train= ros.fit_resample(x_train,y_train)


model= StackingClassifier(
    estimators=[
        ("knn",  KNeighborsClassifier(n_neighbors= 5)),
        ("SVC", SVC(probability=True, random_state= 42)),  
    ],
    n_jobs=-1,
    cv= 5,
    final_estimator= LogisticRegression()
)

model.fit(x_train,y_train)
y_pred= model.predict(x_validate)
test_prediction= model.predict(test_df)
'''
titanic= pd.DataFrame({
    "Name": pd.read_csv("test.csv")['Name'],
    "Survived": test_prediction
})
titanic.to_csv("titanic_pred.csv", index= False)'''

print(classification_report(y_validate, y_pred))