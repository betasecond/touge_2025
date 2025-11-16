import numpy as np


def calcInfoGain(feature, label, index):
    '''
    计算信息增益
    :param feature:测试用例中字典里的feature，类型为ndarray
    :param label:测试用例中字典里的label，类型为ndarray
    :param index:测试用例中字典里的index，即feature部分特征列的索引。该索引指的是feature中第几个特征，如index:0表示使用第一个特征来计算信息增益。
    :return:信息增益，类型float
    '''

    #*********** Begin ***********#

    # 辅助函数：计算熵
    def calcEntropy(labels):
        """
        计算给定标签的熵
        H(X) = -Σ p(x_i) * log2(p(x_i))
        """
        if len(labels) == 0:
            return 0

        # 统计每个类别的数量
        unique_labels, counts = np.unique(labels, return_counts=True)
        # 计算概率
        probabilities = counts / len(labels)

        # 计算熵
        entropy = 0
        for prob in probabilities:
            if prob > 0:  # 避免log(0)
                entropy -= prob * np.log2(prob)

        return entropy

    # 1. 计算总熵 H(D)
    total_entropy = calcEntropy(label)

    # 2. 计算条件熵 H(D|A)
    # 获取指定索引的特征列
    feature_col = feature[:, index]

    # 获取该特征的所有唯一值
    unique_values = np.unique(feature_col)

    # 计算条件熵
    conditional_entropy = 0
    for value in unique_values:
        # 找到特征值等于当前value的样本索引
        mask = (feature_col == value)
        sub_labels = label[mask]

        # 计算该子集的权重（概率）
        weight = len(sub_labels) / len(label)

        # 计算该子集的熵
        sub_entropy = calcEntropy(sub_labels)

        # 累加加权熵
        conditional_entropy += weight * sub_entropy

    # 3. 计算信息增益 g(D,A) = H(D) - H(D|A)
    info_gain = total_entropy - conditional_entropy

    return info_gain

    #*********** End *************#