import numpy as np


class FullyConnected:
    def __init__(self, W, b):
        r'''
        全连接层的初始化。

        Parameter:
        - W: numpy.array, (D_in, D_out)
        - b: numpy.array, (D_out)
        '''
        self.W = W
        self.b = b

        self.x = None
        self.original_x_shape = None

        self.dW = None
        self.db = None

    def forward(self, x):
        r'''
        全连接层的前向传播。

        Parameter:
        - x: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - y: numpy.array, (B, M)
        '''
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        r'''
        全连接层的反向传播

        Parameter:
        - dout: numpy.array, (B, M)

        Return:
        - dx: numpy.array, (B, d1, d2, ..., dk) 与self.original_x_shape形状相同

        另外，还需计算以下结果：
        - self.dW: numpy.array, (N, M) 与self.W形状相同
        - self.db: numpy.array, (M,)
        '''
        ########## Begin ##########
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        dx = dx.reshape(*self.original_x_shape)
        return dx
        ########## End ##########

