4关：scikit-learn线性回归实践 - 波斯顿房价预测
600
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
LinearRegression
编程要求
测试说明
任务描述
本关任务：你需要调用 sklearn 中的线性回归模型，并通过波斯顿房价数据集中房价的13种属性与目标房价对线性回归模型进行训练。我们会调用你训练好的线性回归模型，来对房价进行预测。

相关知识
为了完成本关任务，你需要掌握：1.LinearRegression。

数据集介绍
波斯顿房价数据集共有506条波斯顿房价的数据，每条数据包括对指定房屋的13项数值型特征和目标房价组成。用数据集的80%作为训练集，数据集的20%作为测试集，训练集和测试集中都包括特征和目标房价。
想要使用该数据集可以使用如下代码：

import pandas as pd
#获取训练数据
train_data = pd.read_csv('./step3/train_data.csv')
#获取训练标签
train_label = pd.read_csv('./step3/train_label.csv')
train_label = train_label['target']
#获取测试数据
test_data = pd.read_csv('./step3/test_data.csv')
数据集中部分数据与标签如下图所示：




LinearRegression
LinearRegression的构造函数中有两个常用的参数可以设置：

fit_intercept：是否有截据，如果没有则直线过原点，默认为Ture。
normalize：是否将数据归一化,默认为False。
LinearRegression类中的fit函数用于训练模型，fit函数有两个向量输入：

X：大小为**[样本数量,特征数量]**的ndarray，存放训练样本
Y：值为整型，大小为**[样本数量]**的ndarray，存放训练样本的标签值
LinearRegression类中的predict函数用于预测，返回预测值，predict函数有一个向量输入：

X：大小为**[样本数量,特征数量]**的ndarray，存放预测样本
LinearRegression的使用代码如下：

lr = LinearRegression()
lr.fit(X_train, Y_train)
predict = lr.predict(X_test)
编程要求
使用sklearn构建线性回归模型，利用训练集数据与训练标签对模型进行训练，然后使用训练好的模型对测试集数据进行预测，并将预测结果保存到./step3/result.csv中。保存格式如下：


测试说明
我们会获取你的预测结果与真实标签对比，R2指标高于0.6视为过关。

开始你的任务吧，祝你成功！