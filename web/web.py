from flask import Flask, render_template, url_for,request
from datetime import timedelta
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn import metrics

app = Flask(__name__)
#加载模型
mlp = joblib.load("mlp-module.m")
vectorizer = joblib.load("vectorizer.pkl")
#判断
def judge(payload):
    if payload[0]!='/':
        payload='/'+payload
    payload=[payload]
    x=vectorizer.transform(payload)
    predicted=mlp.predict(x)
    print(predicted)
    if predicted[0]==0:
        return 0
    else:
        return 1

@app.route("/", methods=['GET','POST'])
def main():
    app.logger.info("reflash")
    if request.method == 'POST':
        payload=request.form['payload']
        print(request.form['payload'])
        if judge(payload)==1:
            return render_template('index.html',error="it is an evil payload" )
        else:
           return render_template('index.html',error="it is a normal payload" )
    else:
        return render_template('index.html',error="" )

app.run(host='0.0.0.0', port=50000,debug=True)