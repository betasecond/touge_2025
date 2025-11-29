
夏炘航
gold15480
6.8 使用PyTorch训练MNIST数据集上的卷积神经网络
实验总用时：00:00:03
nav
第1关：使用PyTorch建立网络模型
300
学习内容
参考答案
记录
评论
任务描述
相关知识
PyTorch简介
使用PyTorch建立网络模型的方法
使用PyTorch建立TinyNet网络模型
编程要求
测试说明
任务描述
本关任务：使用 PyTorch 建立网络模型。

相关知识
为了完成本关任务，你需要掌握：

PyTorch 基础；
使用 PyTorch 建立网络模型。
PyTorch简介
进行深度学习研究离不开深度学习框架。目前主流的深度学习框架包括 Google 发布的 TensorFlow、Facebook 发布的 PyTorch 和 Amazon 发布的 MXNet 等。根据深度学习框架的运行方式，通常可以分为静态图设计和动态图设计两种。在静态图设计中，计算图的构建在网络模型的计算之前，对于用户定义的网络模型，深度学习框架会先进行一个“编译”的过程，将网络模型转化成计算图，之后的计算都根据这个计算图来进行。因为计算图在网络模型计算之前已经确定，因此静态图设计可以预先对计算图进行一系列的优化，因此往往具有更好的效率；但是，计算图不能在网络计算的过程中改变，损失了一定的灵活性，同时使得开发和调试变得困难。另一方面，在动态图设计中，计算图的构建在网络模型的计算过程中动态生成，因此非常灵活，开发和调试都非常方便，与一般的 Python 程序无异。但是，因为网络模型计算过程中还要构建计算图，因此效率上会比静态图差一些。通常来说，静态图设计在工业界更为流行，而动态图设计更受到学术界的青睐。

PyTorch 是 Facebook 推出的深度学习框架，自从问世以来，凭借其出色的灵活性和高性能深受欢迎。PyTorch 采用的是动态图设计，因此使用 PyTorch 进行深度学习研究非常高效且灵活。PyTorch 的学习是一个非常庞大的工程，PyTorch 的官方文档和官方指南是学习 PyTorch 的非常好的资料，希望同学们在学习过程中更多的借鉴上面的资料。

使用PyTorch建立网络模型的方法
PyTorch 的基础数据结构是torch.Tensor，tensor 即张量，可以理解为一个多维数组，与我们之前学习计算图时提到的数据节点相对应。而我们之前学习的计算节点，则与torch.autograd.Function相对应。如果将计算节点与其附属的参数放在一起，则构成了torch.nn.Module。如果你仔细阅读了上面的资料，相信你对这些并不陌生。

在 PyTorch 中，torch.nn.Module是我们定义网络模型时最常使用的类。顾名思义，该类定义了一个网络模块。一个网络模型可能由许多网络模块组成，例如卷积层就是一个最基本的网络模块，这在 PyTorch 中由torch.nn.Conv2d给出，这就是一个torch.nn.Module的子类。而整个网络模型更是可以看作是一个最大的网络模块，因此也需要使用torch.nn.Module来定义。在使用torch.nn.Module时，需要实现其构造函数__init__和前向传播函数forward。在构造函数中，需要定义其参数以及子模块。在前向传播函数中，需要实现其前向传播的过程。torch.nn.Module本身是 callable 的，你可以直接对其进行调用，调用时会执行forward方法。值得注意的是，你不需要考虑反向传播的过程，因为 PyTorch 会通过 autograd 机制自动的进行反向传播，前提是你使用的所有计算都是通过 torch 提供的库及其扩展实现的。下面给出了一个感知机的实现，在构造函数中，定义了感知机的权重和偏置，在前向传播函数中，定义了其前向传播的计算：

from torch import nn
class Percepton(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(784, 10) / math.sqrt(784))
        self.bias = nn.Parameter(torch.zeros(10))
    def forward(self, xb):
        return xb @ self.weights + self.bias > 0
使用PyTorch建立TinyNet网络模型
在本实训中，你需要使用 PyTorch 实现一个用于 MNIST 手写数字识别任务的 TinyNet 网络模型。MNIST 数据集包含 60000 张训练图片和 10000 张测试图片，每张图片是一个 28×28 的黑白图像，每张包含一个手写数字。因为数字是从 0-9，所以这个任务可以看作是一个有 10 个类别的分类任务。因为是黑白图像，所以输入图片只有一个通道，是一个 (B,1,28,28) 的 Tensor，其中 B 是 batch size。下图展示了一部分 MNIST 数据集中的数据。



图1
图1 MNIST数据集
你可以自行设计 TinyNet 的结构，这里给出一种参考设计，包含两个卷积层和两个全连接层，整个结构如下表：

序号	类型	参数	输出特征图大小
0	输入	(B, 1, 20, 20)	-
1	卷积层	输出通道32，卷积核大小3x3，步长1，填充1	(B, 32, 20, 20)
2	激活函数	ReLU	(B, 32, 20, 20)
3	卷积层	输出通道64，卷积核大小3x3，步长1，填充1	(B, 64, 20, 20)
4	激活函数	ReLU	(B, 64, 20, 20)
5	池化层	最大值池化，池化窗口2x2，步长2，填充0	(B, 64, 10, 10)
6	Dropout	p=0.25	(B, 64, 10, 10)
7	全连接层	输出神经元128	(B, 128)
4	激活函数	ReLU	(B, 128)
6	Dropout	p=0.5	(B, 128)
7	全连接层	输出神经元10	(B, 10)
需要注意的是，在 6-7 层之间，需要进行一次 flatten 操作使得 Tensor 的形状能够满足全连接层的要求。

编程要求
根据提示，在右侧编辑器 Begin 和 End 之间补充代码，使用 PyTorch 建立网络模型。

测试说明
在本实训中，因为网络模型的初始化是随机的，因此只要你的网络模型的输出的形状是正确的即可，网络模型的训练和有效性验证我们留到下一关进行。

开始你的任务吧，祝你成功！

说点什么
resize-icon
123456789101112131415161718192021
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR


class Net(nn.Module):

测试结果
测试集1
本关最大执行时间：20秒
下一关
run
评测
