import numpy as np


def softmax(x):
    x = x - np.max(x, axis=1, keepdims=True)
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, x, t):
        r'''
        SoftMax + Cross Entropy的前向传播

        Parameter:
        - x: numpy.array, (B, C)
        - t: numpy.array, (B)

        Return:
        - loss: float
        '''
        y = softmax(x)
        batch_size = y.shape[0]
        loss = -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
        self.loss = loss
        self.y = y
        self.t = t
        return loss

    def backward(self):
        r'''
        SoftMax + Cross Entropy的反向传播

        Return:
        - dx: numpy.array, (B, C)
        '''
        ########## Begin ##########
        batch_size = self.t.shape[0]
        dx = self.y.copy()
        dx[np.arange(batch_size), self.t] -= 1
        dx = dx / batch_size
        return dx
        ########## End ##########


class MeanSquaredError:
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None

    def forward(self, y, t):
        r'''
        Mean Squared Error的前向传播

        Parameter:
        - y: numpy.array, (B, N)
        - t: numpy.array, (B, N)

        Return:
        - loss: float
        '''
        loss = 0.5 * np.sum((y - t) ** 2)
        self.loss = loss
        self.y = y
        self.t = t
        return loss

    def backward(self):
        r'''
        Mean Squared Error的反向传播

        Return:
        - dy: numpy.array, (B, N)
        '''
        ########## Begin ##########
        dy = self.y - self.t
        return dy
        ########## End ##########
