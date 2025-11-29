import numpy as np
from utils import im2col


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
        ########## Begin ##########

        ########## End ##########
