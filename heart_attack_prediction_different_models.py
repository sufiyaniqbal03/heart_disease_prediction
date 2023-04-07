# -*- coding: utf-8 -*-
"""heart-attack-prediction-different-models.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Jihz1H-nnseSrZfXgXxSAKjeIQ2OFoL
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

#Importing Dataset
df=pd.read_csv('/content/heart_failure_clinical_records_dataset (1).csv')





"""# EDA"""

df

df.info()

# Finding Null values
df.isnull().sum()

df.describe()

"""# Visualisation"""

sns.distplot(df['platelets'])

sns.heatmap(df.isnull())

"""# Model Building"""

# Splitting data
X=df.iloc[:,0:12]
y=df.iloc[:,-1]

y

#Standardization
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(X)

x

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=1)

# Creating Function
def predict(model):
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    trainac=model.score(xtrain,ytrain)
    testac=model.score(xtest,ytest)
    
    print(f"Triaing Accuracy {trainac}\nTesting Accuracy {testac}")

# KNN
model_knn=KNeighborsClassifier(n_neighbors=6)
model_knn.fit(xtrain,ytrain)
ypred_knn=model_knn.predict(xtest)
trainac_knn=model_knn.score(xtrain,ytrain)
testac_knn=model_knn.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_knn}\nTesting Accuracy {testac_knn}")

trainac=[]
testac=[]

for i in range(1,20):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(xtrain,ytrain)
    ypred=knn.predict(xtest)
    
    trainac.append(knn.score(xtrain,ytrain))
    testac.append(knn.score(xtest,ytest))

sns.set_style(style='darkgrid')

plt.plot(range(1,20), trainac)
plt.plot(range(1,20),testac)
plt.xlabel('Number of K')
plt.ylabel('Accuracy')

# Random Forest Classifier

model_rf=RandomForestClassifier()
model_rf.fit(xtrain,ytrain)
ypred_rf=model_rf.predict(xtest)
trainac_rf=model_rf.score(xtrain,ytrain)
testac_rf=model_rf.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_rf}\nTesting Accuracy {testac_rf}")

from sklearn.svm import SVC

model_SVC_rbf=SVC(kernel='rbf')
model_SVC_rbf.fit(xtrain,ytrain)
ypred_SVC_rbf=model_SVC_rbf.predict(xtest)
trainac_SVC_rbf=model_SVC_rbf.score(xtrain,ytrain)
testac_SVC_rbf=model_SVC_rbf.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_SVC_rbf}\nTesting Accuracy {testac_SVC_rbf}")

model_SVC_poly=SVC(kernel='poly')
model_SVC_poly.fit(xtrain,ytrain)
ypred_SVC_poly=model_SVC_poly.predict(xtest)
trainac_SVC_poly=model_SVC_poly.score(xtrain,ytrain)
testac_SVC_poly=model_SVC_poly.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_SVC_poly}\nTesting Accuracy {testac_SVC_poly}")

model_SVC_linear=SVC(kernel='linear')
model_SVC_linear.fit(xtrain,ytrain)
ypred_SVC_linear=model_SVC_linear.predict(xtest)
trainac_SVC_linear=model_SVC_linear.score(xtrain,ytrain)
testac_SVC_linear=model_SVC_linear.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_SVC_linear}\nTesting Accuracy {testac_SVC_linear}")

model_SVC_sigmoid=SVC(kernel='sigmoid')
model_SVC_sigmoid.fit(xtrain,ytrain)
ypred_SVC_sigmoid=model_SVC_sigmoid.predict(xtest)
trainac_SVC_sigmoid=model_SVC_sigmoid.score(xtrain,ytrain)
testac_SVC_sigmoid=model_SVC_sigmoid.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_SVC_sigmoid}\nTesting Accuracy {testac_SVC_sigmoid}")

from sklearn.linear_model import LogisticRegression

model_LR=LogisticRegression()
model_LR.fit(xtrain,ytrain)
ypred_LR=model_SVC_sigmoid.predict(xtest)
trainac_LR=model_SVC_sigmoid.score(xtrain,ytrain)
testac_LR=model_SVC_sigmoid.score(xtest,ytest)
print(f"Triaing Accuracy {trainac_LR}\nTesting Accuracy {testac_LR}")

from keras.models import Sequential
from keras.layers import Dense 
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

"""model=Sequential()
model.add(Dense(18,imput_dim=8,activation='Sigmoid'))
model.add(Dense(8,activation='Sigmoid'))
model.add(Dense(1,activation='Sigmoid'))
"""

model=Sequential()
model.add(Dense(18,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

history=model.fit(x=xtrain,y=ytrain,validation_split=0.30,epochs=300,batch_size=10)

scores=model.evaluate(xtrain,ytrain)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))

scores=model.evaluate(xtest,ytest)
print("%s: %.2f%%" % (model.metrics_names[1],scores[1]*100))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='upper left')
plt.show()

Models={"Models":["KNN","Random_Forest_Classifier","SVC_rbf","SVC_Poly","SVC_linear","SVC_sigmoid","Logistic_Regression","ANN"],\
       "Training_Accuracy":[model_knn.score(xtrain,ytrain),model_rf.score(xtrain,ytrain),model_SVC_rbf.score(xtrain,ytrain),model_SVC_poly.score(xtrain,ytrain),model_SVC_linear.score(xtrain,ytrain),model_SVC_sigmoid.score(xtrain,ytrain),model_SVC_sigmoid.score(xtrain,ytrain),model.evaluate(xtrain,ytrain)],\
       "Testing_Accuracy":[model_knn.score(xtest,ytest),model_rf.score(xtest,ytest),model_SVC_rbf.score(xtest,ytest),model_SVC_poly.score(xtest,ytest),model_SVC_linear.score(xtest,ytest),model_SVC_sigmoid.score(xtest,ytest),model_SVC_sigmoid.score(xtest,ytest),model.evaluate(xtest,ytest)]}

Scores=pd.DataFrame(Models)

Scores

ypred_LR=model_SVC_sigmoid.predict([xtest[21]])

ypred_LR

