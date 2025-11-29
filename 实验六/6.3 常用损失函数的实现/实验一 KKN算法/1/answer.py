import numpy as np


def softmax(x):
    x = x - np.max(x, axis=1, keepdims=True)
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None

    def forward(self, x, t):
        r'''
        SoftMax + Cross Entropy的前向传播

        Parameter:
        - x: numpy.array, (B, C)
        - t: numpy.array, (B)

        Return:
        - loss: float
        '''
        ########## Begin ##########

        ########## End ##########


class MeanSquaredError:
    def __init__(self):
        self.loss = None

    def forward(self, y, t):
        r'''
        Mean Squared Error的前向传播

        Parameter:
        - y: numpy.array, (B, N)
        - t: numpy.array, (B, N)

        Return:
        - loss: float
        '''
        ########## Begin ##########

        ########## End ##########
