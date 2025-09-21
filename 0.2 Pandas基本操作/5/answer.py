# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import numpy as np
import  pandas as pd

def add_way():
    '''
    返回值:
    df3: 一个DataFrame类型数据
    '''

    # df1,df2是DataFrame类型数据
    df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
    df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    # 使用 .add() 方法进行相加，并使用 fill_value 参数指定填充值
    # 在计算时，如果 df1 或 df2 中某个位置没有值，就会用 4 来代替
    df3 = df1.add(df2, fill_value=4)

    # ********** End **********#

    # 返回df3
    return df3
