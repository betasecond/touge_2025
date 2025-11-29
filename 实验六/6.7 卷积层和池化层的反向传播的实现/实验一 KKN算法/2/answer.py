import numpy as np
from utils import im2col, col2im


class MaxPool:
    def __init__(self, pool_h, pool_w, stride=1, pad=0):
        r'''
        池化层的初始化

        Parameter:
        - pool_h: int
        - pool_h: int
        - stride: int
        - pad: int
        '''
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

        self.x = None
        self.arg_max = None

    def forward(self, x):
        r'''
        池化层的前向传播

        Parameter:
        - x: numpy.array, (B, C, H, W)

        Return:
        - y: numpy.array, (B, C, H', W')
             H' = (H - Kh + 2P) / S + 1
             W' = (W - Kw + 2P) / S + 1
        '''
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h + 2 * self.pad) / self.stride)
        out_w = int(1 + (W - self.pool_w + 2 * self.pad) / self.stride)

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(-1, self.pool_h * self.pool_w)

        arg_max = np.argmax(col, axis=1)
        out = np.max(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max

        return out

    def backward(self, dout):
        r'''
        池化层的反向传播

        Parameter:
        - dout: numpy.array, (B, C', H', W')

        Return:
        - dx: numpy.array, (B, C, H, W)
        '''
        ########## Begin ##########

        ########## End ##########
