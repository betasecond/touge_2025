import numpy as np

def calcGini(feature, label, index):
    '''
    计算基尼系数
    :param feature:测试用例中字典里的feature，类型为ndarray
    :param label:测试用例中字典里的label，类型为ndarray
    :param index:测试用例中字典里的index，即feature部分特征列的索引。该索引指的是feature中第几个特征，如index:0表示使用第一个特征来计算信息增益。
    :return:基尼系数，类型float
    '''

    #********* Begin *********#

    # 辅助函数：计算数据集的基尼系数
    def calcGiniIndex(labels):
        """
        计算基尼系数 Gini(D) = 1 - Σ(pk^2)
        其中 pk 是第k个类别在数据集中所占的比例
        """
        if len(labels) == 0:
            return 0

        # 统计每个类别的数量
        unique_labels, counts = np.unique(labels, return_counts=True)
        # 计算每个类别的比例
        probabilities = counts / len(labels)

        # 计算基尼系数: Gini = 1 - Σ(p_k^2)
        gini = 1 - np.sum(probabilities ** 2)

        return gini

    # 计算基于特征的基尼系数 Gini(D, a)
    # 获取指定特征列
    feature_col = feature[:, index]

    # 获取特征的所有唯一值
    unique_values = np.unique(feature_col)

    # 计算加权基尼系数
    gini_da = 0
    total_samples = len(feature)

    for value in unique_values:
        # 找到特征值为value的样本
        mask = (feature_col == value)
        sub_labels = label[mask]

        # 计算权重
        weight = len(sub_labels) / total_samples

        # 计算子集的基尼系数
        sub_gini = calcGiniIndex(sub_labels)

        # 累加加权基尼系数
        gini_da += weight * sub_gini

    return gini_da

    #********* End *********#