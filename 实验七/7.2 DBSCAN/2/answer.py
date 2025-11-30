#encoding=utf8
import numpy as np
import random

#寻找eps邻域内的点
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
    k = 0  # 簇编号
    n = X.shape[0]
    cluster = [-1] * n  # 初始化所有点为噪声点(-1)
    visited = [False] * n  # 标记点是否被访问过

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        neighbors = findNeighbor(i, X, eps)

        if len(neighbors) < min_Pts:
            # 非核心点，暂时标记为噪声
            continue

        # 发现核心点，创建新簇
        cluster[i] = k
        seeds = list(neighbors)

        j = 0
        while j < len(seeds):
            q = seeds[j]
            if not visited[q]:
                visited[q] = True
                q_neighbors = findNeighbor(q, X, eps)
                if len(q_neighbors) >= min_Pts:
                    # q也是核心点，扩展邻域
                    seeds.extend(q_neighbors)
            if cluster[q] == -1:
                cluster[q] = k
            j += 1
        k += 1
    #********* End *********#
    return cluster