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

    def forward(self, x):
        r'''
        全连接层的前向传播。

        Parameter:
        - x: numpy.array, (B, d1, d2, ..., dk)

        Return:
        - y: numpy.array, (B, M)
        '''
        ########## Begin ##########
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out
        ########## End ##########

