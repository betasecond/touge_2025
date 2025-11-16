from sklearn.ensemble import RandomForestClassifier

def digit_predict(train_image, train_label, test_image):
    '''
    实现功能：训练模型并输出预测结果
    :param train_image: 包含多条训练样本的样本集，类型为ndarray,shape为[-1, 8, 8]
    :param train_label: 包含多条训练样本标签的标签集，类型为ndarray
    :param test_image: 包含多条测试样本的测试集，类型为ndarry
    :return: test_image对应的预测标签，类型为ndarray
    '''

    #************* Begin ************#

    # 1. 将训练图像从[-1, 8, 8]变形为[-1, 64]
    # 每个8x8的图像展平为64个特征
    train_image_flat = train_image.reshape(train_image.shape[0], -1)

    # 2. 将测试图像从[-1, 8, 8]变形为[-1, 64]
    test_image_flat = test_image.reshape(test_image.shape[0], -1)

    # 3. 创建随机森林分类器
    # 增加树的数量到100，使用auto(sqrt)作为max_features
    # 设置random_state保证结果可复现
    clf = RandomForestClassifier(n_estimators=100, max_features='auto', random_state=42)

    # 4. 训练模型
    clf.fit(train_image_flat, train_label)

    # 5. 预测测试集
    result = clf.predict(test_image_flat)

    return result

    #************* End **************#