
夏炘航
gold11060
4 决策树
实验总用时：00:00:01
nav
第3关：使用ID3算法构建决策树
600
学习内容
参考答案
记录
评论
任务描述
相关知识
ID3算法
使用决策树进行预测
编程要求
测试说明
任务描述
本关任务：补充python代码，完成DecisionTree类中的fit和predict函数。

相关知识
为了完成本关任务，你需要掌握：

ID3算法构造决策树的流程；

如何使用构造好的决策树进行预测。

ID3算法
ID3算法其实就是依据特征的信息增益来构建树的。其大致步骤就是从根结点开始，对结点计算所有可能的特征的信息增益，然后选择信息增益最大的特征作为结点的特征，由该特征的不同取值建立子结点，然后对子结点递归执行上述的步骤直到信息增益很小或者没有特征可以继续选择为止。

因此，ID3算法伪代码如下：

#假设数据集为D，标签集为A，需要构造的决策树为tree
def ID3(D, A):
    if D中所有的标签都相同:
        return 标签
    if 样本中只有一个特征或者所有样本的特征都一样:
        对D中所有的标签进行计数
        return 计数最高的标签
        
    计算所有特征的信息增益
    选出增益最大的特征作为最佳特征(best_feature)
    将best_feature作为tree的根结点
    得到best_feature在数据集中所有出现过的值的集合(value_set)
    for value in value_set:
        从D中筛选出best_feature=value的子数据集(sub_feature)
        从A中筛选出best_feature=value的子标签集(sub_label)
        #递归构造tree
        tree[best_feature][value] = ID3(sub_feature, sub_label)
    return tree
使用决策树进行预测
决策树的预测思想非常简单，假设现在已经构建出了一棵用来决策是否买西瓜的决策树。




并假设现在在水果店里有这样一个西瓜，其属性如下：

瓤是否够红	够不够冰	是否便宜	是否有籽
是	否	是	否
那买不买这个西瓜呢？只需把西瓜的属性代入决策树即可。决策树的根结点是瓤是否够红，所以就看西瓜的属性，经查看发现够红，因此接下来就看够不够冰。而西瓜不够冰，那么看是否便宜。发现西瓜是便宜的，所以这个西瓜是可以买的。

因此使用决策树进行预测的伪代码也比较简单，伪代码如下：

#tree表示决策树，feature表示测试数据
def predict(tree, feature):
    if tree是叶子结点:
        return tree
    根据feature中的特征值走入tree中对应的分支
    if 分支依然是课树:
        result = predict(分支, feature)
    return result
编程要求
填写fit(self, feature, label)函数，实现ID3算法，要求决策树保存在self.tree中。其中：

feature：训练集数据，类型为ndarray，数值全为整数；

label：训练集标签，类型为ndarray，数值全为整数。

填写predict(self, feature)函数，实现预测功能，并将标签返回，其中：

feature：测试集数据，类型为ndarray，数值全为整数。（PS：feature中有多条数据）
测试说明
只需完成fit与predict函数即可，程序内部会调用您所完成的fit函数构建模型并调用predict函数来对数据进行预测。预测的准确率高于0.92视为过关。(PS:若self.tree is None则会打印决策树构建失败)

开始你的任务吧，祝你成功！

说点什么
7
resize-icon
12345678910111213141516171819202122
import numpy as np
class DecisionTree(object):
    def __init__(self):
        #决策树模型
        self.tree = {}
    def calcInfoGain(self, feature, label, index):
        '''
        计算信息增益
        :param feature:测试用例中字典里的feature，类型为ndarray
        :param label:测试用例中字典里的label，类型为ndarray

测试结果
测试集1
本关最大执行时间：120秒
上一关
下一关
run
评测
