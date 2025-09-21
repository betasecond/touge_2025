import pandas as pd
from datetime import datetime


def task1():
    '''
    任务：创建以 2021 年1 月1 日为开始的 12 条时间索引，相邻索引间隔时间长度为一个月。
    '''
    ########## Begin ##########
    # 使用 pd.date_range 创建时间序列
    # start='2021-01-01' 指定开始日期
    # periods=12 指定生成12个时间点
    # freq='M' 指定频率为每个月的月末
    result = pd.date_range('2021-01-01', periods=12, freq='M')
    ########## End ##########

    return result


def task2():
    '''
    任务：在 2021 年 1 月 1 日到 2021 年 3 月 1 日间，每隔一周创建一条索引。
    '''
    ########## Begin ##########
    # start 和 end 参数定义时间范围
    # freq='W' 指定频率为每周，默认为周日
    result = pd.date_range('2021-01-01', '2021-03-01', freq='W')
    ########## End ##########

    return result


def task3():
    '''
    任务：给定以时间为索引的 Series 对象，查找索引时间在 2021 年 1 月内的所有记录。
    '''
    start = datetime(2021, 1, 1)
    end = datetime(2021, 3, 1)
    rng = pd.date_range(start, end, freq='W')
    ts = pd.Series(range(len(rng)), index=rng)

    ########## Begin ##########
    # Pandas 支持使用部分字符串对时间序列进行切片
    # '2021-01' 会匹配该年份和月份下的所有日期
    result = ts['2021-01']
    ########## End ##########

    return result
