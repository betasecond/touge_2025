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
        ########## Begin ##########

        ########## End ##########


class ReLU:
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
        ########## Begin ##########

        ########## End ##########
