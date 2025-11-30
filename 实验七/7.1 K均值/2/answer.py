#encoding=utf8
import numpy as np
#计算样本间距离
def distance(x, y, p=2):
    '''
    input:x(ndarray):第一个样本的坐标
          y(ndarray):第二个样本的坐标
          p(int):等于1时为曼哈顿距离，等于2时为欧氏距离
    output:distance(float):x到y的距离      
    '''
    #********* Begin *********#
    # 计算x和y之间差的绝对值的p次方
    diff = np.abs(x - y)
    # 计算最终的距离值
    dis = np.power(np.sum(np.power(diff, p)), 1/p)
    #********* End *********#
    return dis
    
#计算质心
def cal_Cmass(data):
    '''
    input:data(ndarray):数据样本
    output:mass(ndarray):数据样本质心
    '''
    #********* Begin *********#
    # 计算数据样本的质心（即每个维度的平均值）
    Cmass = np.mean(data, axis=0)
    #********* End *********#
    return Cmass

#计算每个样本到质心的距离，并按照从小到大的顺序排列
def sorted_list(data,Cmass):
    '''
    input:data(ndarray):数据样本
          Cmass(ndarray):数据样本质心
    output:dis_list(list):排好序的样本到质心距离
    '''
    #********* Begin *********#
    # 初始化一个空列表，用于存储距离
    dis_list = []
    # 遍历数据样本中的每个样本
    for i in range(data.shape[0]):
        # 计算当前样本到质心的距离，并添加到列表中
        dis = distance(data[i], Cmass)
        dis_list.append(dis)
    # 对距离列表进行排序
    dis_list.sort()
    #********* End *********#
    return dis_list
