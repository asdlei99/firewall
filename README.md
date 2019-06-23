# firewall
我使用的环境是 python3.6，scikit-learn 的版本是 0.20.0，scipy的版本是1.1.0。

CountVectorizer-LogisticRegression.py是采用词袋模型和逻辑回归的代码。

evalurl.py是存放我自己写的特征提取函数的代码。

mlp-test.py是使用mlp-module.m这个模型进行测试。

my-svm.py是我自己写的特征提取和SVM分类的代码，训练好模型保持为my-svm-module.m。

svm-test.py是使用my-svm-module.m这个模型进行测试。

TfidfVectorizer-LogisticRegression.py文件是最开始的采取tf-idf和逻辑回归的代码。

TfidfVectorizer-MLP.py是采用tf-idf和MLP的代码，也是目前为止准确率和召回率最高的代码,模型保存为mlp-module.m。

TfidfVectorizer-svm.py文件是采用tf-idf和SVM的代码，训练好模型保持为td-idf-svm-module.m。