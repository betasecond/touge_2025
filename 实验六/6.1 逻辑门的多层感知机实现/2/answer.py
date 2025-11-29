import numpy as np


def mlp_and(x1, x2):
    x = np.array([x1, x2]).astype(np.float32)
    weight = np.array([0.5, 0.5]).astype(np.float32)
    bias = -0.7
    y = np.dot(weight, x) + bias
    if y <= 0:
        return 0
    else:
        return 1


def mlp_or(x1, x2):
    x = np.array([x1, x2]).astype(np.float32)
    weight = np.array([0.5, 0.5]).astype(np.float32)
    bias = -0.2
    y = np.dot(weight, x) + bias
    if y <= 0:
        return 0
    else:
        return 1


def mlp_nand(x1, x2):
    x = np.array([x1, x2]).astype(np.float32)
    weight = np.array([-0.5, -0.5]).astype(np.float32)
    bias = 0.7
    y = np.dot(weight, x) + bias
    if y <= 0:
        return 0
    else:
        return 1


def mlp_xor(x1, x2):
    r'''
    使用多层感知机实现异或逻辑门。
    '''
    ########## Begin ##########
    # 逻辑修改如下：
    # 第一层：计算 NAND 和 OR
    s_nand = mlp_nand(x1, x2)  # 只有当 (1,1) 时为 0，其余为 1
    s_or = mlp_or(x1, x2)      # 只有当 (0,0) 时为 0，其余为 1
    
    # 第二层：将上述结果进行 AND
    # 只有当 NAND 和 OR 同时为 1 时（即 (0,1) 或 (1,0)），结果才为 1
    y = mlp_and(s_nand, s_or)
    
    return y
    ########## End ##########