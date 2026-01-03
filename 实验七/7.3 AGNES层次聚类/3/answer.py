#encoding=utf8
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

def Agglomerative_cluster(data):
    '''
    对红酒数据进行聚类
    :param data: 数据集，类型为ndarray
    :return: 聚类结果，类型为ndarray
    '''

    #********* Begin *********#
    
    # 1. 数据预处理：由于层次聚类依赖距离计算，需要先对数据进行标准化
    # 使每个特征的均值为0，方差为1
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # 2. 实例化 AgglomerativeClustering
    # 根据要求，簇的数量 n_clusters 为 3
    # 提示：sklearn 官方参数名为 n_clusters，而非题目示例代码中误写的 k
    agnes = AgglomerativeClustering(n_clusters=3)

    # 3. 训练模型并获取聚类结果
    result = agnes.fit_predict(data_scaled)

    #********* End *********#

    return result