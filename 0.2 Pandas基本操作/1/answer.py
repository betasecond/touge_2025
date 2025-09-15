# 引入numpy库
import numpy as np
# 定义cnmda函数
def cnmda(m,n):
    '''
    创建numpy数组
    参数：
    m:第一维的长度
    n: 第二维的长度
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0

    # 请在此添加创建多维数组的代码并赋值给ret
    #********** Begin *********#
    # 创建一个长度为 n 的列表作为数组的每一行
    row = [y for y in range(n)]
    # 将该行重复 m 次，并转换为 numpy 数组
    ret = np.array([row] * m)
    #********** End **********#

    return ret