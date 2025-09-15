# 引入numpy库
import numpy as np

def task1(A):
    """
    任务1: 计算矩阵 A 的平方根并与标量 2 相加
    参数:
    A: 输入的Numpy数组或列表
    返回值:
    task1_result: 任务1的结果
    """
    # 为确保输入的兼容性，首先将输入转换为Numpy数组
    A = np.array(A)
    # 计算矩阵 A 的平方根并与标量 2 相加
    task1_result = np.sqrt(A) + 2
    return task1_result

def task2(A):
    """
    任务2: 将矩阵 A 开根号后的小数部分与原矩阵 A 相加
    参数:
    A: 输入的Numpy数组或列表
    返回值:
    task2_result: 任务2的结果
    """
    # 为确保输入的兼容性，首先将输入转换为Numpy数组
    A = np.array(A)
    # np.modf 会将小数和整数部分以两个独立数组的形式返回
    fractional_part, integer_part = np.modf(np.sqrt(A))
    task2_result = fractional_part + A
    return task2_result

def task3(A):
    """
    任务3: 使用通用函数 numpy.dot() 计算矩阵 A 与矩阵 A 转置的矢量积
    参数:
    A: 输入的Numpy数组或列表
    返回值:
    task3_result: 任务3的结果
    """
    # 为确保输入的兼容性，首先将输入转换为Numpy数组
    A = np.array(A)
    # 使用通用函数 numpy.dot() 计算矩阵 A 与矩阵 A 转置的矢量积
    task3_result = np.dot(A, A.T)
    return task3_result

