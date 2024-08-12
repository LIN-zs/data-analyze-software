# coding=utf-8
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False



from soil.project.data import originaldata

data=originaldata(r'C:\Users\16609\Desktop\research\Pb 定标\LIBS.csv')

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = data.getttdata(0.2)


# 调用PSO_SVR.py文件
import PSO_SVR

# 获取返回的调参后的模型
svr = PSO_SVR.optimize_svm(X_train, y_train, X_test, y_test)
# 训练
svr.fit(X_train, y_train)
# 预测
result = svr.predict(X_test)

# 计算模型在测试数据上的得分，通常使用R^2（决定系数）作为评估指标。
score = svr.score(X_test, y_test)

# 存储测试数据的真实标签和预测结果
y_testRON = []
resultRON = []
for i in range(len(result)):
    y_testRON.append(y_test[i])
    resultRON.append(result[i])

# 计算了模型在训练数据上的得分。
score_train = svr.score(X_train, y_train)
result_train = svr.predict(X_train)

# 存储训练数据的真实标签和预测结果
y_trainRON = []
resultRON_train = []
for i in range(len(result_train)):
    y_trainRON.append(y_train[i])
    resultRON_train.append(result_train[i])

##可视化
fig = plt.figure()
fig.subplots_adjust(hspace=0.4)
plt.subplot(2, 1, 1)
plt.plot(np.arange(len(result_train)), y_trainRON, "bo-", label="True value 冲蚀速率  -train")
plt.plot(np.arange(len(result_train)), resultRON_train, "ro-", label="Predict value 冲蚀速率  -train")
plt.title(f"train_SVM---R^2:{score_train}")
plt.legend(loc="best")
plt.subplot(2, 1, 2)
plt.plot(np.arange(len(result)), y_testRON, "bo-", label="True value 冲蚀速率")
plt.plot(np.arange(len(result)), resultRON, "ro-", label="Predict value 冲蚀速率")
plt.title(f"test_SVM---R^2:{score}")
plt.legend(loc="best")
plt.show()

##可视化标准误差
# test
RON = np.array(resultRON)
# train
RONtrain = np.array(resultRON_train)

RE_RONtest = abs(y_testRON - RON) / y_testRON

RE_RONtrain = abs(y_trainRON - RONtrain) / y_trainRON

plt.figure()
plt.plot(np.arange(len(RE_RONtrain)), RE_RONtrain, "ro-", label="RE value 冲蚀速率  -train")
plt.plot(np.arange(len(RE_RONtrain), len(RE_RONtrain) + len(RE_RONtest)), RE_RONtest, "bo-",
         label="RE value 冲蚀速率  -test")
plt.title('Relative Error')
plt.legend(loc="best")
plt.show()
