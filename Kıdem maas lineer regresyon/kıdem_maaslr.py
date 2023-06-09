# -*- coding: utf-8 -*-
"""Kıdem_maasLR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GeA3IukhS72mvHgd0pMcpmRwpJIblwBI
"""

from google.colab import files
uploaded=files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Kıdem_maas=pd.read_csv('dataset.csv')
Kıdem_maas.head()

deneyim=Kıdem_maas['Kidem'].values
maas=Kıdem_maas['Maas'].values
uzunluk=len(deneyim)
deneyim=deneyim.reshape((uzunluk,1))

import sklearn.linear_model as ln
reg=ln.LinearRegression()

import sklearn.model_selection as ms
X_train,X_test,y_train,y_test=ms.train_test_split(deneyim,maas,test_size=1/3)

reg.fit(X_train,y_train)

y_pred=reg.predict(X_train)
print("deneyimler ",X_test)
print("Maaşlar ",y_pred)

import sklearn.metrics as nt

predictions=reg.predict(X_test)
score=nt.r2_score(y_test,predictions)
print("SCORE: ", score)

plt.scatter(deneyim,maas,color="b")
plt.ylabel("MAAŞ")
plt.xlabel("KIDEM")
plt.scatter(X_test,predictions,color="r")