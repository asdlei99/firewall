# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 10:51:14 2018

@author: peter
"""
import time


from sklearn.feature_extraction.text import TfidfVectorizer
import os
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import urllib.parse
from sklearn.externals import joblib

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
vectorizer = TfidfVectorizer(min_df = 0.0, 
        analyzer="char", sublinear_tf=True, ngram_range=(1,3)) 
X = vectorizer.fit_transform(queries)
joblib.dump(vectorizer, 'new.vectorizer.pkl')
#交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

badCount = len(badQueries)
validCount = len(validQueries)


#使用MLP进行训练
mlp= MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(5, 5), random_state=1)
mlp.fit(X_train, y_train)

#保存模型到本地
joblib.dump(mlp, "new.mlp-module.m")
#评估模型

predicted=mlp.predict(X_test)


print("Bad samples: %d" % badCount)
print("Good samples: %d" % validCount)
print("Accuracy: %f" % mlp.score(X_test, y_test))  
print("Precision: %f" % metrics.precision_score(y_test, predicted))
print("Recall: %f" % metrics.recall_score(y_test, predicted))

time1 = time.time()
print("TF-IDF and MLP: 总共花费 {0} s".format( time1-time0))