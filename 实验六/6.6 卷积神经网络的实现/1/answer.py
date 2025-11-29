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
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = 1 + int((H + 2 * self.pad - FH) / self.stride)
        out_w = 1 + int((W + 2 * self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
        col_W = self.W.reshape(FN, -1).T

        out = np.dot(col, col_W) + self.b
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out
        ########## End ##########

