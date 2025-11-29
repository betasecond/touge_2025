from sklearn.neighbors import KNeighborsClassifier

def classification(train_feature, train_label, test_feature):
    '''
    使用KNeighborsClassifier对test_feature进行分类
    :param train_feature: 训练集数据
    :param train_label: 训练集标签
    :param test_feature: 测试集数据
    :return: 测试集预测结果
    '''

    #********* Begin *********#

    # 1. 创建/实例化一个kNN分类器对象
    # 我们这里使用默认参数，即 n_neighbors=5
    clf = KNeighborsClassifier()

    # 2. 使用训练数据来训练分类器
    # .fit()方法是sklearn中所有模型的标准训练函数
    clf.fit(train_feature, train_label)

    # 3. 使用训练好的分类器对测试数据进行预测
    predict_result = clf.predict(test_feature)

    # 4. 返回预测结果
    return predict_result

    #********* End *********#