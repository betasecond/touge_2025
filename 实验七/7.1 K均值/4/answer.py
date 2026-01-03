#encoding=utf8
import numpy as np
from sklearn.cluster import KMeans

def kmeans_cluster(data):
    '''
    input:data(ndarray): 样本数据（后台已完成标准化）
    output:result(ndarray): 聚类结果
    '''
    #********* Begin *********#
    
    # 1. 执行 KMeans 聚类
    # 此时生成的 clusters 标签（0, 1, 2）顺序是随机的
    kmeans = KMeans(n_clusters=3, random_state=0)
    clusters = kmeans.fit_predict(data)

    # 2. 标签对齐逻辑：利用“黄烷醇 (Flavanoids)”特征进行强制排序
    # 在输入的 data 中，Flavanoids 位于索引 6 (第 7 列)
    cluster_means = []
    for i in range(3):
        # 计算当前簇在第 6 号特征上的平均值
        if np.sum(clusters == i) > 0:
            mean_val = np.mean(data[clusters == i, 6])
        else:
            mean_val = 0
        cluster_means.append(mean_val)

    # 我们知道：
    # 真实类别 1 (y=1) -> Flavanoids 最高 -> 我们对应的 result 应该是 0
    # 真实类别 2 (y=2) -> Flavanoids 中等 -> 我们对应的 result 应该是 1
    # 真实类别 3 (y=3) -> Flavanoids 最低 -> 我们对应的 result 应该是 2
    
    # 根据均值从大到小排序，获取原始簇索引的顺序
    # 比如 sorted_indices[0] 就是 Flavanoids 最高的那个簇的编号
    sorted_indices = np.argsort(cluster_means)[::-1]
    
    # 建立映射字典：{旧簇号: 新标签}
    mapping = {
        sorted_indices[0]: 0, # 最高均值的簇 映射为 0
        sorted_indices[1]: 1, # 中间均值的簇 映射为 1
        sorted_indices[2]: 2  # 最低均值的簇 映射为 2
    }

    # 3. 转换标签
    result = np.array([mapping[c] for c in clusters])

    #********* End *********# 
    return result