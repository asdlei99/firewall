# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:06:14 2018

@author: peter
"""
from sklearn.feature_extraction.text import CountVectorizer
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import urllib.parse
import time
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
#使用词袋模型
vectorizer = CountVectorizer(min_df=0.0)  
X = vectorizer.fit_transform(queries)
#交叉验证
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)  

badCount = len(badQueries)
validCount = len(validQueries)

# 逻辑回归进行分类训练
lgs = LogisticRegression(class_weight="balanced")
lgs.fit(X_train, y_train)  

#评估模型

predicted = lgs.predict(X_test)


print("Bad samples: %d" % badCount)
print("Good samples: %d" % validCount)
print("Accuracy: %f" % lgs.score(X_test, y_test))  
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))

time1 = time.time()
print("CountVectorizer and LogisticRegression: 总共花费 {0} s".format( 
        time1-time0))


