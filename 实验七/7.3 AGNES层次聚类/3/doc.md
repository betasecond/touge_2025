
夏炘航
gold18075
7.3 AGNES层次聚类
实验总用时：00:00:00
nav
第3关：红酒聚类
300
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
AgglomerativeClustering
编程要求
测试说明
任务描述
本关任务：sklearn中的AgglomerativeClustering类实现了AGNES算法，本关你需要使用 sklearn 中AgglomerativeClustering来对红酒数据进行聚类。

相关知识
为了完成本关任务，你需要掌握：AgglomerativeClustering

数据集介绍
数据集为一份红酒数据，一共有178个样本，每个样本有13个特征，这里不会提供你红酒的标签，你需要自己根据这13个特征对红酒进行聚类，部分数据如下图：




数据获取代码：

import pandas as pd
data_frame = pd.read_csv('./step3/dataset.csv', header=0)
AgglomerativeClustering
AgglomerativeClustering的构造函数中有两个常用的参数可以设置：

n_clusters：将数据聚成n_clusters个类
linkage：设置AGNES聚类时使用最小簇间距离、最大簇间距离还是平均距离。传入ward表示最小簇间距离，传入complete表示最大簇间距离，传入average表示平均距离
AgglomerativeClustering类中的fit_predict函数用于训练模型并获取聚类结果，fit_predict函数有一个向量输入：

X：数据集，形状为**[样本数量,特征数量]**的ndarray
AgglomerativeClustering的使用代码如下：

from sklearn.cluster import AgglomerativeClustering
agnes = AgglomerativeClustering(k=5)
# 注意：x为ndarray
result = agnes.fit_predict(x)
编程要求
在Begin-End区域填写Agglomerative_cluster(data)函数完成红酒数据聚类任务，簇的数量为3。其中：

data：数据样本，类型为ndarray，shape=[样本数量, 特征数量]

return: 聚类结果，类型为ndarray

注意：直接使用原始数据进行聚类的效果可能不太理想，你可能需要对数据进行预处理。

提示：AGNES算法需要计算距离，想想什么样的预处理方式对依赖距离的算法有好的效果。

测试说明
只需返回聚类结果即可，程序内部会检测您的代码，吻合度高于0.9视为过关。

开始你的任务吧，祝你成功！

说点什么
1
resize-icon
123456789101112131415
#encoding=utf8
from sklearn.cluster import AgglomerativeClustering

def Agglomerative_cluster(data):
    '''
    对红酒数据进行聚类
    :param data: 数据集，类型为ndarray
    :return: 聚类结果，类型为ndarray
    '''


测试结果
测试集1
本关最大执行时间：120秒
上一关
run
评测
