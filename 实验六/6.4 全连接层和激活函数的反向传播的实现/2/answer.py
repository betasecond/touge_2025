import numpy as np


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        r'''
        Sigmoid激活函数的前向传播。

        Parameter:
        - x: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - y: numpy.array, (B, d1, d2, ..., dk)
        '''
        out = 1. / (1. + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        r'''
        sigmoid的反向传播

        Parameter:
        - dout: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - dx: numpy.array, (B, d1, d2, ..., dk)
        '''
        ########## Begin ##########
        dx = dout * (1.0 - self.out) * self.out
        return dx
        ########## End ##########


class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        r'''
        ReLU激活函数的前向传播。

        Parameter:
        - x: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - y: numpy.array, (B, d1, d2, ..., dk)
        '''
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out

    def backward(self, dout):
        r'''
        relu的反向传播

        Parameter:
        - dout: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - dx: numpy.array, (B, d1, d2, ..., dk)
        '''
        ########## Begin ##########
        dout[self.mask] = 0
        dx = dout
        return dx
        ########## End ##########

