# 引入numpy库
import numpy as np
# 定义opeadd函数
def opeadd(m,b,n):
    '''实现加法
    参数：
    m:是一个数组
    b:是一个列表
    n:是列表中的索引
    你需要做的是 m+b[n]
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0
    # 请在此添加 创建多维数组 的代码 并赋值给ret
    #********** Begin *********#
    ret = m + b[n]
    #********** End **********#

    return ret
# 定义opemul函数
def opemul(m,b,n):
    '''实现乘法
    参数：
    m:是一个数组
    b:是一个列表
    n:是列表中的索引
    你需要做的是 m*b[n]
    返回值:
    ret: 一个numpy数组
    '''
    ret = 0
    # 请在此添加 创建多维数组 的代码 并赋值给ret
    #********** Begin *********#
    # 注意：根据函数名和测试用例，这里的操作应该是乘法，而不是加法
    ret = m * b[n]
    #********** End **********#
    return ret
