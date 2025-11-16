
夏炘航
gold13260
5.1 随机森林
实验总用时：00:00:01
nav
第3关：手写数字识别
200
学习内容
参考答案
记录
评论
任务描述
相关知识
数据简介
RandomForestClassifier
编程要求
测试说明
任务描述
本关任务：使用 sklearn 中的 RandomForestClassifier 类完成手写数字识别任务。请不要修改Begin-End段之外的代码。

相关知识
为了完成本关任务，你需要掌握如何使用 sklearn 提供的 RandomForestClassifier 类。

数据简介
本关使用的是手写数字数据集，该数据集有 1797 个样本，每个样本包括 8*8 像素（实际上是一条样本有 64 个特征，每个像素看成是一个特征，每个特征都是 float 类型的数值）的图像和一个 [0, 9] 整数的标签。比如下图的标签是 2 ：

 

RandomForestClassifier
 RandomForestClassifier 的构造函数中有两个常用的参数可以设置：

 n_estimators ：森林中决策树的数量；

 criterion ：构建决策树时，划分节点时用到的指标。有 gini （基尼系数）, entropy (信息增益)。若不设置，默认为 gini；

 max_depth ：决策树的最大深度，如果发现模型已经出现过拟合，可以尝试将该参数调小。若不设置，默认为 None；

 max_features ：随机选取特征时选取特征的数量，一般传入 auto 或者 log2，默认为 auto ， auto 表示 max_features=sqrt(训练集中特征的数量) ；log2 表示 max_features=log2(训练集中特征的数量)。 

 RandomForestClassifier 类中的 fit 函数实现了随机森林分类器训练模型的功能，predict 函数实现了模型预测的功能。

其中 fit 函数的参数如下：

X ：大小为 [样本数量,特征数量] 的 ndarry，存放训练样本；
Y ：值为整型，大小为 [样本数量] 的 ndarray，存放训练样本的分类标签。
而 predict 函数有一个向量输入：

X ：大小为 [样本数量,特征数量] 的 ndarry，存放预测样本。
 RandomForestClassifier 的使用代码如下：

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=50)
clf.fit(X_train, Y_train)
result = clf.predict(X_test)
编程要求
在右侧区域的 begin-end 之间填写digit_predict(train_image, train_label, test_image)函数完成手写数字分类任务，其中：

 train_image ：包含多条训练样本的样本集，类型为 ndarray ， shape 为 [-1, 8, 8] ，在喂给分类器之前请记得将其变形；

 train_label ：包含多条训练样本标签的标签集，类型为 ndarray；

 test_image ：包含多条测试样本的测试集，类型为 ndarray；

 return ： test_image 对应的预测标签，类型为 ndarray。 

测试说明
只需完成 digit_predict 函数即可，程序内部会检测您的代码，预测正确率高于 0.98 视为过关。

开始你的任务吧，祝你成功！

说点什么
resize-icon
1234567891011121314
from sklearn.ensemble import RandomForestClassifier

def digit_predict(train_image, train_label, test_image):
    '''
    实现功能：训练模型并输出预测结果
    :param train_image: 包含多条训练样本的样本集，类型为ndarray,shape为[-1, 8, 8]
    :param train_label: 包含多条训练样本标签的标签集，类型为ndarray
    :param test_image: 包含多条测试样本的测试集，类型为ndarry
    :return: test_image对应的预测标签，类型为ndarray

测试结果
测试集1
本关最大执行时间：120秒
上一关
run
评测
