import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
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


def plot_loss(history):
    plt.plot(history.history['loss'], label= 'loss')
    plt.plot(history.history['val_loss'], label= 'val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Binary crossentropy')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_accuracy(history):
    plt.plot(history.history.get('accuracy', history.history.get('acc')), label='accuracy')
    if 'val_accuracy' in history.history or 'val_acc' in history.history:
        plt.plot(history.history.get('val_accuracy', history.history.get('val_acc')), label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()    


model= tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation= 'relu', input_shape = (10,)),
    tf.keras.layers.Dense(32, activation= 'relu'),
    tf.keras.layers.Dense(1, activation= 'sigmoid')
])

model.compile(optimizer= tf.optimizers.Adam(0.001), loss= 'binary_crossentropy',
              metrics= ['accuracy'])

history = model.fit(
    x_train,y_train, epochs= 100, batch_size= 32, validation_split= 0.2, verbose=0
)
