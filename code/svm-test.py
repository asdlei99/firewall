# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:22:50 2018

@author: peter
"""
import re
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn import metrics
import eval_url
x = []
y = []




def read_file(filename, data, isEvil):
    global y
    try:
        file_object = open(filename, 'r', encoding='UTF-8')
        file = file_object.readlines()
        for line in file:
            data.append(eval_url.get_feature(line))
        if isEvil:
            y += [1 for _ in range(0, len(file))]
        else:
            y += [0 for _ in range(0, len(file))]
    finally:
        file_object.close()


read_file('badqueries.txt', x, 1)#读取恶意请求
read_file('goodqueries.txt', x, 0)#读取正常请求
#加载模型
clf = joblib.load("my-svm-module.m")
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42) 

    

predicted = clf.predict(x_test)


print("Accuracy: %f" % clf.score(x_test, y_test))  
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))


print("Accuracy :", metrics.accuracy_score(predicted, y_test))
