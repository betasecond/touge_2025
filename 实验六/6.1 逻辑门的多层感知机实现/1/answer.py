import numpy as np


def mlp_and(x1, x2):
    r'''
    使用感知机实现与逻辑门。

    参数：
    - x1: int (0 or 1)
    - x2: int (0 or 1)

    输出：
    - y: int (0 or 1)
        y = x1 and x2
    '''
    ########## Begin ##########
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1
    ########## End ##########


def mlp_or(x1, x2):
    r'''
    使用感知机实现或逻辑门。

    参数：
    - x1: int (0 or 1)
    - x2: int (0 or 1)

    输出：
    - y: int (0 or 1)
        y = x1 or x2
    '''
    ########## Begin ##########
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1
    ########## End ##########


def mlp_nand(x1, x2):
    r'''
    使用感知机实现与非逻辑门。

    参数：
    - x1: int (0 or 1)
    - x2: int (0 or 1)

    输出：
    - y: int (0 or 1)
        y = x1 nand x2
    '''
    ########## Begin ##########
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1
    ########## End ##########

