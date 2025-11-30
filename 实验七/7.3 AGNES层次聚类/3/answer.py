#encoding=utf8
from sklearn.cluster import AgglomerativeClustering

def Agglomerative_cluster(data):
    '''
    对红酒数据进行聚类
    :param data: 数据集，类型为ndarray
    :return: 聚类结果，类型为ndarray
    '''

    #********* Begin *********#
    model = AgglomerativeClustering(n_clusters=3, linkage='average')
    result = model.fit_predict(data)
    return result
    #********* End *********#

