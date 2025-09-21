# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd

def create_series():
    '''
    返回值:
    series_a: 一个Series类型数据
    series_b: 一个Series类型数据
    dict_a：  一个字典类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    # 任务1：创建一个名为series_a的series数组
    series_a = Series([1, 2, 5, 7], index=['nu', 'li', 'xue', 'xi'])

    # 任务2：创建一个名为dict_a的字典
    dict_a = {'ting': 1, 'shuo': 2, 'du': 32, 'xie': 44}

    # 任务3：将dict_a字典转化成名为series_b的series数组
    series_b = Series(dict_a)

    # ********** End **********#

    # 返回series_a,dict_a,series_b
    return series_a, dict_a, series_b
