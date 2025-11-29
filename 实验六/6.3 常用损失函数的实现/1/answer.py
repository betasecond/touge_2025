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
        batch_size = x.shape[0]
        p = softmax(x)
        self.y = p
        self.t = t
        # 交叉熵损失
        loss = -np.log(p[np.arange(batch_size), t] + 1e-7)
        self.loss = np.mean(loss)
        return self.loss
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
        self.y = y
        self.t = t
        diff = y - t
        self.loss = 0.5 * np.sum(diff ** 2)
        return self.loss
        ########## End ##########
