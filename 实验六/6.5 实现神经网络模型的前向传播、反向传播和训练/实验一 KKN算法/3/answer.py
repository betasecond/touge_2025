import numpy
from layers import Convolution, Relu, FullyConnected, MaxPool, SoftmaxWithLoss


class TinyNet:
    def __init__(self, W_conv1, b_conv1, W_conv2, b_conv2, W_fc, b_fc):
        self.conv1 = Convolution(W_conv1, b_conv1, stride=1, pad=1)
        self.relu1 = Relu()
        self.pool1 = MaxPool(2, 2, stride=2, pad=0)
        self.conv2 = Convolution(W_conv2, b_conv2, stride=1, pad=1)
        self.relu2 = Relu()
        self.pool2 = MaxPool(2, 2, stride=2, pad=0)
        self.fc = FullyConnected(W_fc, b_fc)
        self.loss = SoftmaxWithLoss()

    def forward(self, x, t):
        x = self.conv1.forward(x)
        x = self.relu1.forward(x)
        x = self.pool1.forward(x)
        x = self.conv2.forward(x)
        x = self.relu2.forward(x)
        x = self.pool2.forward(x)
        x = self.fc.forward(x)
        loss = self.loss.forward(x, t)
        return x, loss

    def backward(self):
        dx = self.loss.backward()
        dx = self.fc.backward(dx)
        dx = self.pool2.backward(dx)
        dx = self.relu2.backward(dx)
        dx = self.conv2.backward(dx)
        dx = self.pool1.backward(dx)
        dx = self.relu1.backward(dx)
        dx = self.conv1.backward(dx)
        return self.conv1.dW, self.conv1.db, self.conv2.dW, self.conv2.db, self.fc.dW, self.fc.db


def train_one_iter(W_conv1, b_conv1, W_conv2, b_conv2, W_fc, b_fc, x, t, learning_rate):
    network = TinyNet(W_conv1, b_conv1, W_conv2, b_conv2, W_fc, b_fc)
    out, loss = network.forward(x, t)
    dW_conv1, db_conv1, dW_conv2, db_conv2, dW_fc, db_fc = network.backward()

    ########## Begin ##########

    ########## End ##########

    return new_W_conv1, new_b_conv1, new_W_conv2, new_b_conv2, new_W_fc, new_b_fc
