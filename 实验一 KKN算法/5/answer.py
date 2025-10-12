from sklearn.preprocessing import StandardScaler

def scaler(data):
    '''
    返回标准化后的红酒数据
    :param data: 红酒数据对象
    :return: 标准化后的红酒数据，类型为ndarray
    '''

    #********* Begin *********#

    # 1. 实例化StandardScaler对象
    # This creates the tool we'll use for scaling.
    s_scaler = StandardScaler()

    # 2. 从数据对象中提取特征数据 (data.data)
    #    然后调用 fit_transform 方法。
    #    该方法会计算每一列的均值和标准差，然后应用标准化公式。
    standardized_data = s_scaler.fit_transform(data.data)

    # 3. 返回经过标准化处理后的数据
    return standardized_data

    #********* End **********#