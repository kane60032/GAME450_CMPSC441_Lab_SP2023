""" Lab 8: Save people
You can save people from heart disease by training a model to predict whether a person has heart disease or not.
The dataset is available at src/lab8/heart.csv
Train a model to predict whether a person has heart disease or not and test its performance.
You can usually improve the model by normalizing the input data. Try that and see if it improves the performance. 
"""
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
#from sklearn.preprocessing import normalize
import pandas as pd
import numpy as np

data = pd.read_csv("src/lab8/heart.csv")

#accuracyMax = 0.0
#maxIteration = 0
#for iteration in range(100):

#while iteration <= 3:
#    iteration += 1
        
# Transform the categorical variables into dummy variables.
print(data.head())
string_col = data.select_dtypes(include="object").columns
df = pd.get_dummies(data, columns=string_col, drop_first=False)
print(data.head())

y = df.HeartDisease.values
x = df.drop(["HeartDisease"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25
)

""" Train a sklearn model here. """

sklearn_model = KNeighborsClassifier(n_neighbors=5)
sklearn_model.fit(x,y)

# Accuracy
print("Accuracy of model: {}\n".format(sklearn_model.score(x_test, y_test)))


""" Improve the model by normalizing the input data. """

# NOMRALIZATION = (data - min) / (max - mix) 
#x_test = ((x_test - x_test.min()) / x_test.max() - x_test.min())
#x = ((x - x.min()) / x.max() - x.min())
#x_test = normalize(x_test)
#x = normalize(x)
x_test = preprocessing.normalize(x_test, norm='l1')
x = preprocessing.normalize(x, norm='l1')
sklearn_model = KNeighborsClassifier(n_neighbors=5)
sklearn_model.fit(x,y)

#accuracyTemp = sklearn_model.score(x_test, y_test)
#if accuracyTemp > accuracyMax:
#    accuracyMax = accuracyTemp
#    maxIteration = iteration
print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_test, y_test)))


#print("THE BEST ITERATION WAS WITH ITERATION #", maxIteration, " AND HAD AN ACCURACY OF ", accuracyMax)