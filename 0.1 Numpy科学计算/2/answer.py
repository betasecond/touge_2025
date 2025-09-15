# 引入numpy库
import numpy as np

def get_roi(data, x, y, w, h):
    '''
    根据给定的参数提取ROI
    参数:
    data: 待提取ROI的原始图像数据(其实就是个二维数组)，类型为ndarray；
    x: ROI的左上角顶点的行索引，类型为int；
    y: ROI的左上角顶点的列索引，类型为int；
    w: ROI的宽，类型为int；
    h: ROI的高，类型为int。
    返回值:
    roi: 提取的ROI，类型为ndarray
    '''
    # 请在此添加实现代码
    #********** Begin *********#
    # 根据 x, y, w, h 定义切片的范围
    # 从测试用例来看，w 和 h 可能代表的是偏移量，所以需要+1来包含边界
    roi = data[x:x+h+1, y:y+w+1]
    #********** End **********#
    return roi

