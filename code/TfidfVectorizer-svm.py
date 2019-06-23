# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:22:50 2018

@author: peter
"""
import time
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from sklearn.model_selection import train_test_split
import urllib.parse
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn import metrics
#from mlxtend.plotting import plot_decision_regions
time0 = time.time()
def loadFile(name):#读取文件
    directory = str(os.getcwd())
    filepath = os.path.join(directory, name)
    with open(filepath, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    data = list(set(data))
    result = []
    for d in data:
        d = str(urllib.parse.unquote(d))
        result.append(d)
    return result


badQueries = loadFile('badqueries.txt')#读取恶意请求
validQueries = loadFile('goodqueries.txt')#读取正常请求
#去重

badQueries = list(set(badQueries))
validQueries = list(set(validQueries))
allQueries = badQueries + validQueries
#打标签
yBad = [1 for i in range(0, len(badQueries))]  
yGood = [0 for i in range(0, len(validQueries))]
y = yBad + yGood
queries = allQueries

#TF-IDF进行特征提取
vectorizer = TfidfVectorizer(min_df = 0.0, analyzer="char", sublinear_tf=True, ngram_range=(1,3)) 
X = vectorizer.fit_transform(queries)
#交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

badCount = len(badQueries)
validCount = len(validQueries)




#clf = svm.NuSVC(nu=0.1).fit(X_train, y_train)
clf = svm.LinearSVC(C=10, max_iter=3000).fit(X_train, y_train)
#joblib.dump(clf, "td-idf-svm-module.m")

predicted = clf.predict(X_test)


print("Accuracy: %f" % clf.score(X_test, y_test))  
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))


print("Accuracy :", metrics.accuracy_score(predicted, y_test))

time1 = time.time()
print("TF-IDF and SVM: 总共花费 {0} s".format( time1-time0))
