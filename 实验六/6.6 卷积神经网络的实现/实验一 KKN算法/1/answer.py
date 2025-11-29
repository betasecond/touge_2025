import numpy as np
from utils import im2col


class Convolution:
    def __init__(self, W, b, stride=1, pad=0):
        r'''
        卷积层的初始化

        Parameter:
        - W: numpy.array, (C_out, C_in, K_h, K_w)
        - b: numpy.array, (C_out)
        - stride: int
        - pad: int
        '''
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        r'''
        卷积层的前向传播

        Parameter:
        - x: numpy.array, (B, C, H, W)

        Return:
        - y: numpy.array, (B, C', H', W')
             H' = (H - Kh + 2P) / S + 1
             W' = (W - Kw + 2P) / S + 1
        '''
        ########## Begin ##########

        ########## End ##########

