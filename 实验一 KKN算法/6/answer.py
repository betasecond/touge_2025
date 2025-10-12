from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

def classification(train_feature, train_label, test_feature):
    '''
    对test_feature进行红酒分类
    :param train_feature: 训练集数据，类型为ndarray
    :param train_label: 训练集标签，类型为ndarray
    :param test_feature: 测试集数据，类型为ndarray
    :return: 测试集数据的分类结果
    '''

    #********* Begin *********#

    # 1. 创建标准化工具并处理数据
    scaler = StandardScaler()

    # 使用训练集来拟合（fit）scaler，并转换（transform）训练集
    scaled_train_feature = scaler.fit_transform(train_feature)

    # 使用同一个已经拟合好的scaler来转换测试集
    scaled_test_feature = scaler.transform(test_feature)

    # 2. 创建并训练kNN分类器
    # 使用默认参数的KNeighborsClassifier
    knn = KNeighborsClassifier()

    # 使用处理（标准化）过的数据来训练模型
    knn.fit(scaled_train_feature, train_label)

    # 3. 使用训练好的模型进行预测
    # 对处理（标准化）过的测试数据进行预测
    predictions = knn.predict(scaled_test_feature)

    # 4. 返回预测结果
    return predictions

    #********* End **********#