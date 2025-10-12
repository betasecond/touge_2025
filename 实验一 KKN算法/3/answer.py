from sklearn.neighbors import KNeighborsRegressor

def regression(train_feature, train_label, test_feature):
    '''
    使用KNeighborsRegressor对test_feature进行分类
    :param train_feature: 训练集数据
    :param train_label: 训练集标签
    :param test_feature: 测试集数据
    :return: 测试集预测结果
    '''

    #********* Begin *********#

    # 1. 创建/实例化一个kNN回归器对象
    # 同样，我们使用默认参数（k=5）
    reg = KNeighborsRegressor()

    # 2. 使用训练数据来训练回归器
    # .fit() 方法存储训练数据，为预测做准备
    reg.fit(train_feature, train_label)

    # 3. 使用训练好的回归器对测试数据进行预测
    # 对于回归，预测值是其近邻目标值的平均值
    predict_result = reg.predict(test_feature)

    # 4. 返回预测结果
    return predict_result

    #********* End *********#