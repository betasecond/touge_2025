import numpy as np

def alcohol_mean(data):
    '''
    返回红酒数据中红酒的酒精平均含量
    :param data: 红酒数据对象
    :return: 酒精平均含量，类型为float
    '''

    #********* Begin *********#

    # 从数据对象中获取所有特征数据，这是一个NumPy数组
    all_features = data['data']

    # 酒精含量是第一个特征，即第0列
    # 使用切片 [:, 0] 来选取所有行的第0列
    alcohol_column = all_features[:, 0]

    # 使用numpy的mean函数计算该列的平均值
    mean_value = np.mean(alcohol_column)

    # 返回计算出的平均值
    return mean_value

    #********* End **********#