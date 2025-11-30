#encoding=utf8
from sklearn.cluster import KMeans

def kmeans_cluster(data):
    '''
    input:data(ndarray):样本数据
    output:result(ndarray):聚类结果
    '''
    #********* Begin *********#
    model = KMeans(n_clusters=3, n_init=10, random_state=42)
    result = model.fit_predict(data)
    #********* End *********#
    return result



