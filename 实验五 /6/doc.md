
夏炘航
gold13260
5.2 Adaboost算法
实验总用时：00:00:00
nav
第3关：sklearn中的Adaboost
300
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
AdaBoostClassifier
编程要求
测试说明
任务描述
本关任务：你需要调用 sklearn 中的 Adaboost 模型，并通过癌细胞数据集对 Adaboost 模型进行训练。我们会调用你训练好的 Adaboost 模型，来对未知的癌细胞进行识别。

相关知识
为了完成本关任务，你需要掌握：1. AdaBoostClassifier。

数据集介绍
乳腺癌数据集，其实例数量是 569 ，实例中包括诊断类和属性，帮助预测的属性一共 30 个，各属性包括为 radius  半径（从中心到边缘上点的距离的平均值），texture  纹理（灰度值的标准偏差）等等，类包括： WDBC-Malignant  恶性和  WDBC-Benign  良性。用数据集的 80% 作为训练集，数据集的 20% 作为测试集，训练集和测试集中都包括特征和诊断类。

想要使用该数据集可以使用如下代码：

from sklearn.datasets import load_breast_cancer
#加载数据
cancer = load_breast_cancer()
#获取特征与标签
x,y = cancer['data'],cancer['target']
#划分训练集与测试集
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=666)
数据集中部分数据与标签如下图所示：

 

 

AdaBoostClassifier
 AdaBoostClassifier 的构造函数中有四个常用的参数可以设置：

 algorithm ：这个参数只有 AdaBoostClassifier 有。主要原因是scikit-learn 实现了两种 Adaboost 分类算法， SAMME 和 SAMME.R。两者的主要区别是弱学习器权重的度量， SAMME.R 使用了概率度量的连续值，迭代一般比 SAMME 快，因此 AdaBoostClassifier 的默认算法 algorithm 的值也是 SAMME.R；

 n_estimators ：弱学习器的最大迭代次数。一般来说 n_estimators 太小，容易欠拟合，n_estimators 太大，又容易过拟合，一般选择一个适中的数值。默认是 50；

 learning_rate ：AdaBoostClassifier 和 AdaBoostRegressor 都有，即每个弱学习器的权重缩减系数 ν，默认为 1.0；

 base_estimator ：弱分类学习器或者弱回归学习器。理论上可以选择任何一个分类或者回归学习器，不过需要支持样本权重。我们常用的一般是 CART 决策树或者神经网络 MLP。

和 sklearn 中其他分类器一样，AdaBoostClassifier 类中的 fit 函数用于训练模型，fit 函数有两个向量输入：

 X ：大小为**[样本数量,特征数量]**的 ndarray，存放训练样本；

 Y ：值为整型，大小为**[样本数量]**的 ndarray，存放训练样本的分类标签。

AdaBoostClassifier 类中的 predict 函数用于预测，返回预测标签， predict 函数有一个向量输入：

 X ：大小为**[样本数量,特征数量]**的 ndarray，存放预测样本
AdaBoostClassifier 的使用代码如下：

ada=AdaBoostClassifier(n_estimators=5,learning_rate=1.0)
ada.fit(train_data,train_label)
predict = ada.predict(test_data)
编程要求
在 begin-end 区域内填写ada_classifier(train_data,train_label,test_data)函数完成癌细胞识别任务，其中：

train_data：训练样本；
train_label：训练标签；
test_data：测试样本。
测试说明
只需返回预测结果即可，程序内部会检测您的代码，预测正确率高于 95% 视为过关。

开始你的任务吧，祝你成功！

说点什么
resize-icon
1234567891011121314151617181920212223
#encoding=utf8
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
def ada_classifier(train_data,train_label,test_data):
    '''
    input:train_data(ndarray):训练数据
          train_label(ndarray):训练标签
          test_data(ndarray):测试标签
    output:predict(ndarray):预测结果
    '''

测试结果
测试集1
本关最大执行时间：20秒
上一关
run
评测
