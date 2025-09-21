# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def delete_duplicated():
    '''
    返回值:
    df2: 一个DataFrame类型数据
    '''

    # df1是DataFrame类型数据
    df1 = DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [1, 1, 2, 3, 3, 4, 4]})
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    # 使用 drop_duplicates() 方法去除重复的行
    df2 = df1.drop_duplicates()

    # ********** End **********#

    # 返回df2
    return df2
