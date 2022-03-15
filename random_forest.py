# -*- coding: utf-8 -*-
"""Random Forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/jonahcoutinho/Machine-Learning/blob/main/Random_Forest.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.datasets import load_digits

digits=load_digits()

'''plt.gray()
for i in range(5):
  plt.matshow(digits.images[i])

dir(digits)
'''
df=pd.DataFrame(digits.data)
df['target']=digits.target
#df

xtrain,xtest,ytrain,ytest=train_test_split(df.drop('target',axis='columns'),df.target,test_size=0.2)

'''from sklearn.model_selection import GridSearchCV
model=RandomForestClassifier()
param={'bootstrap': [True, False],
 'max_depth': [10, 20, 30, 40, 50, None],
 'n_estimators': [10,20,30,40,50,60,100,200],
 'criterion':['gini', 'entropy']} 
grid=GridSearchCV(model,param,cv=5)
grid.fit(xtrain,ytrain)
grid.best_params_

"""YES it takes Time!!"""
'''
model=RandomForestClassifier(bootstrap=False,criterion='gini',n_estimators=200,max_depth=40)
model.fit(xtrain,ytrain)

'''pred=model.predict(xtest)
cm=confusion_matrix(pred,ytest)

import seaborn as sns
plt.figure(figsize=(10,10))
sns.heatmap(cm,annot=True)
'''
print(model.score(xtest,ytest))



