#encoding=utf8
import numpy as np
import random

#寻找eps邻域内的点 (已给出)
def findNeighbor(j,X,eps):
    N=[]
    for p in range(X.shape[0]):   #找到所有领域内对象
        temp=np.sqrt(np.sum(np.square(X[j]-X[p])))   #欧氏距离
        if(temp<=eps):
            N.append(p)
    return N
    
#dbscan算法
def dbscan(X,eps,min_Pts):
    '''
    input:X(ndarray):样本数据
          eps(float):eps邻域半径
          min_Pts(int):eps邻域内最少点个数
    output:cluster(list):聚类结果
    '''
    #********* Begin *********#
    n_samples = X.shape[0]
    # 初始化聚类结果：-2 表示未访问，-1 表示噪声，0及以上表示簇标签
    cluster = [-2] * n_samples
    cluster_id = 0
    
    for i in range(n_samples):
        # 如果该点已经处理过，则跳过
        if cluster[i] != -2:
            continue
            
        # 获取当前点的邻域点索引
        neighbors = findNeighbor(i, X, eps)
        
        # 步骤1：判断是否为核心对象
        if len(neighbors) < min_Pts:
            # 暂时标记为噪声点
            cluster[i] = -1
        else:
            # 步骤2：创建一个新簇，并开始扩展
            cluster[i] = cluster_id
            
            # 使用集合作为种子队列，寻找所有密度可达的点
            seeds = set(neighbors)
            if i in seeds:
                seeds.remove(i)
            
            while seeds:
                # 弹出队列中的一个点进行检查
                j = seeds.pop()
                
                # 如果该点之前被标记为噪声，它现在成了当前簇的边界点
                if cluster[j] == -1:
                    cluster[j] = cluster_id
                
                # 如果该点还未被访问
                if cluster[j] != -2:
                    continue
                
                # 将该点加入当前簇
                cluster[j] = cluster_id
                
                # 步骤3：如果 j 也是核心点，则将其邻域点加入种子队列（密度溢出）
                j_neighbors = findNeighbor(j, X, eps)
                if len(j_neighbors) >= min_Pts:
                    seeds.update(j_neighbors)
            
            # 完成一个簇的扩展，标签自增
            cluster_id += 1

    #********* End *********#
    return cluster