
夏炘航
gold13260
5.1 随机森林
实验总用时：00:00:01
nav
第2关：随机森林算法流程
300
学习内容
参考答案
记录
评论
任务描述
相关知识
随机森林的训练流程
随机森林的预测流程
编程要求
测试说明
任务描述
本关任务：补充 python 代码，完成 RandomForestClassifier 类中的 fit 和 predict 函数。请不要修改 Begin-End 段之外的代码。

相关知识
为了完成本关任务，你需要掌握随机森林的训练与预测流程

随机森林的训练流程
随机森林是 Bagging 的一种扩展变体，随机森林的训练过程相对与 Bagging 的训练过程的改变有：

基学习器： Bagging 的基学习器可以是任意学习器，而随机森林则是以决策树作为基学习器。
随机属性选择：假设原始训练数据集有 10 个特征，从这 10 个特征中随机选取 k 个特征构成训练数据子集，然后将这个子集作为训练集扔给决策树去训练。其中 k 的取值一般为 log2(特征数量) 。
这样的改动通常会使得随机森林具有更加强的泛化性，因为每一棵决策树的训练数据集是随机的，而且训练数据集中的特征也是随机抽取的。如果每一棵决策树模型的差异比较大，那么就很容易能够解决决策树容易过拟合的问题。

随机森林训练过程伪代码如下：

#假设数据集为D，标签集为A，需要构造的决策树为tree
def fit(D, A):
    models = []
    for i in range(决策树的数量):
        有放回的随机采样数据，得到数据集sample_D和标签sample_A
        从采样到的数据中随机抽取K个特征构成训练集sub_D
        构建决策树tree
        tree.fit(sub_D, sample_A)
        models.append(tree)
    return models
随机森林的预测流程
随机森林的预测流程与 Bagging 的预测流程基本一致，如果是回归，就将结果基学习器的预测结果全部加起来算平均；如果是分类，就投票，票数最多的结果作为最终结果。但需要注意的是，在预测时所用到的特征必须与训练模型时所用到的特征保持一致。例如，第 3 棵决策树在训练时用到了训练集的第 2，5，8 这 3 个特征。那么在预测时也要用第 2，5，8 这 3 个特征所组成的测试集传给第 3 棵决策树进行预测。

编程要求
在 begin-end 中完成 RandomForestClassifier 类中的 fit 和 predict 函数。分类器可使用 sklearn 提供的 DecisionTreeClassifier ，要求模型保存在 self.models 中。

 fit 函数用于随机森林的训练过程，其中：

feature ：训练集数据，类型为 ndarray；
label ：训练集标签，类型为 ndarray。
 predict 函数，实现预测功能，并将标签返回，其中：

feature ：测试集数据，类型为 ndarray 。（PS：feature中有多条数据）
测试说明
只需完成 fit 与 predict 函数即可，程序内部会调用您所完成的 fit 函数构建模型并调用 predict 函数来对数据进行预测。预测的准确率高于 0.9 视为过关。

开始你的任务吧，祝你成功！

说点什么
resize-icon
1234567891011121314151617181920212223

import numpy as np

#建议代码，也算是Begin-End中的一部分
from collections import  Counter
from sklearn.tree import DecisionTreeClassifier

class RandomForestClassifier():
    def __init__(self, n_model=10):
        '''

测试结果
测试集1
本关最大执行时间：120秒
上一关
下一关
run
评测
