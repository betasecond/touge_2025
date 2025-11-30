import numpy as np

def AGNES(feature, k):
    '''
    AGNES聚类并返回聚类结果，量化距离时请使用簇间最大欧氏距离
    假设数据集为`[1, 2], [10, 11], [1, 3]]，那么聚类结果可能为`[[1, 2], [1, 3]], [[10, 11]]]
    :param feature:数据集，类型为ndarray
    :param k:表示想要将数据聚成`k`类，类型为`int`
    :return:聚类结果，类型为list
    '''

    #********* Begin *********#
    # 初始化：每个样本作为一个簇
    clusters = [[sample.tolist()] for sample in feature]

    while len(clusters) > k:
        # 找到距离最近的两个簇（使用最大距离）
        min_dist = np.inf
        merge_i, merge_j = 0, 1

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # 计算簇间最大距离
                max_dist = 0
                for p1 in clusters[i]:
                    for p2 in clusters[j]:
                        dist = np.sqrt(np.sum((np.array(p1) - np.array(p2)) ** 2))
                        if dist > max_dist:
                            max_dist = dist
                if max_dist < min_dist:
                    min_dist = max_dist
                    merge_i, merge_j = i, j

        # 合并两个簇
        clusters[merge_i].extend(clusters[merge_j])
        del clusters[merge_j]

    return clusters
    #********* End *********#
