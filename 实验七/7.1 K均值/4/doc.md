
夏炘航
gold20175
7.1 K均值
实验总用时：00:00:14
nav
第4关：sklearn中的k-means
300
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
本关任务：：你需要调用 sklearn 中的K-means模型，对红酒数据进行聚类。

相关知识
为了完成本关任务，你需要掌握：1.KMeans。

数据集介绍
数据集为一份红酒数据，一共有178个样本，每个样本有13个特征，这里不会提供你红酒的标签，你需要自己根据这13个特征对红酒进行聚类，部分数据如下图：



编程要求
请仔细阅读右侧代码，结合相关知识，在 Begin-End 区域内进行代码补充，完使用 sklearn 中的K-means模型实现红酒聚类任务。

测试说明
平台会对你的代码进行运行测试，如果实际输出结果与预期结果相同，则通关；反之，则 GameOver。

说点什么
1
resize-icon
12345678910111213141516
#encoding=utf8
from sklearn.cluster import KMeans

def kmeans_cluster(data):
    '''
    input:data(ndarray):样本数据
    output:result(ndarray):聚类结果
    '''
    #********* Begin *********#


测试结果
测试集1
本关最大执行时间：20秒
上一关
run
评测
