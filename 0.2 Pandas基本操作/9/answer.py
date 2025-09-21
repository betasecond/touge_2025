# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def create_dataframe():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    # 任务1: 创建一个五行三列的DataFrame
    # 首先定义数据和行/列索引
    data = {'states': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
            'years': [2000, 2001, 2002, 2001, 2002],
            'pops': [1.5, 1.7, 3.6, 2.4, 2.9]}
    index = ['one', 'two', 'three', 'four', 'five']
    columns = ['states', 'years', 'pops']

    # 使用 pd.DataFrame 创建 df1
    df1 = DataFrame(data, index=index, columns=columns)

    # 任务2: 给df1添加新列
    df1['new_add'] = [7, 4, 5, 8, 2]

    # ********** End **********#

    #返回df1
    return df1
