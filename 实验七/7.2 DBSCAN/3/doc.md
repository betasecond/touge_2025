
夏炘航
gold18075
7.2 DBSCAN
实验总用时：00:00:00
nav
第3关：sklearn中的DBSCAN
300
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
DBSCAN
编程要求
测试说明
任务描述
本关任务：你需要调用 sklearn 中的 DBSCAN 模型，对非球状数据进行聚类。

相关知识
为了完成本关任务，你需要掌握：1.DBSCAN。

数据集介绍
在这里，我们使用sklearn中的datasets.make_circles方法自己制作了一份数据，一共100个样本。这100个样本不提供标签，你需要使用 DBSACN 算法对其进行聚类，数据分布如下图：




数据生成代码：

from sklearn import datasets
X,y=datasets.make_moons(n_samples=100,noise=0.005,random_state=666)
DBSCAN
DBSCAN的构造函数中有两个常用的参数可以设置：

eps：eps 邻域半径大小；

min_samples：即 Minpts，eps邻域内样本最少数目；和sklearn中其他聚类器一样，DBSCAN不允许对新的数据进行预测，DBSCAN类中的fit_predict函数用于训练模型并获取聚类结果，fit_predict函数有一个向量输入：

X：大小为 [样本数量,特征数量] 的ndarray，存放训练样本。

DBSCAN的使用代码如下：

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.5,min_samples =10)
result = dbscan.fit_predict(x)
编程要求
填写data_cluster(data)函数完成非球状数据聚类任务，其中：

data：数据样本。
测试说明
只需返回聚类结果即可，程序内部会检测您的代码，吻合度高于95%视为过关。

开始你的任务吧，祝你成功！

说点什么
1
resize-icon
12345678910111213141516171819202122
#encoding=utf8
from sklearn.cluster import DBSCAN
def data_cluster(data):
    '''
    input: data(ndarray) :数据
    output: result(ndarray):聚类结果
    '''
    #********* Begin *********#

    #********* End *********#                     

测试结果
测试集1
本关最大执行时间：120秒
上一关
run
评测
