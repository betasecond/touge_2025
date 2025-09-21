# -*- coding: utf-8 -*-
from pandas import Series,DataFrame
import  pandas as pd
# pandas版本原因显示，设置列名仅显示4列
pd.set_option('display.max_columns', 4)


def read_csv_data():
    '''
    返回值:
    df1: 一个DataFrame类型数据
    length1: 一个int类型数据
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#

    # 任务1: 将CSV文件中的数据导入到df1中
    df1 = pd.read_csv('test3/uk_rain_2014.csv')

    # 任务2: 将列名修改为指定列表
    df1.columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']

    # 任务3: 计算df1的总行数
    length1 = len(df1)

    # ********** End **********#
    #返回df1,length1
    return df1,length1
