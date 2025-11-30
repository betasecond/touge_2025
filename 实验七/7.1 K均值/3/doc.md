
夏炘航
gold18065
7.1 K均值
实验总用时：00:00:00
nav
第3关：k-means算法流程
700
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
编程要求
测试说明
任务描述
本关任务：使用Python实现k-means算法，并根据红酒的13个特征对红酒数据进行聚类。

相关知识
为了完成本关任务，你需要掌握：1.k-means算法原理，2.k-means算法流程，3.如何确定k的值。

数据集介绍
数据集为一份红酒数据，一共有178个样本，每个样本有13个特征，这里不会提供你红酒的标签，你需要自己根据这13个特征对红酒进行聚类，部分数据如下图：



编程要求
请仔细阅读右侧代码，结合相关知识，在 Begin-End 区域内进行代码补充，完使用Python实现k-means算法的任务。

测试说明
平台会对你的代码进行运行测试，如果实际输出结果与预期结果相同，则通关；反之，则 GameOver。

说点什么
2
resize-icon
1234567891011121314151617181920
#encoding=utf8
import numpy as np

# 计算一个样本与数据集中所有样本的欧氏距离的平方
def euclidean_distance(one_sample, X):
    one_sample = one_sample.reshape(1, -1)
    distances = np.power(np.tile(one_sample, (X.shape[0], 1)) - X, 2).sum(axis=1)
    return distances


测试结果
测试集1
本关最大执行时间：20秒
上一关
下一关
run
评测
