#encoding=utf8
from sklearn.cluster import DBSCAN
def data_cluster(data):
    '''
    input: data(ndarray) :数据
    output: result(ndarray):聚类结果
    '''
    #********* Begin *********#
    model = DBSCAN(eps=0.2, min_samples=5)
    result = model.fit_predict(data)
    return result
    #********* End *********#                     
                            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                