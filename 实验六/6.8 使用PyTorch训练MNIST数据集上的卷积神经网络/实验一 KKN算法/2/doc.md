
夏炘航
gold15480
6.8 使用PyTorch训练MNIST数据集上的卷积神经网络
实验总用时：00:00:00
nav
第2关：使用PyTorch训练网络模型
300
学习内容
参考答案
记录
评论
任务描述
相关知识
使用PyTorch载入数据
使用PyTorch训练网络模型
编程要求
测试说明
任务描述
本关任务：使用 PyTorch 训练网络模型。

相关知识
为了完成本关任务，你需要掌握：

使用 PyTorch 载入数据；
使用 PyTorch 训练网络模型。
使用PyTorch载入数据
训练网络模型首先需要准备数据。在 PyTorch 中，载入数据需要用到两个类，分别是torch.utils.data.Dataset和torch.utils.data.DataLoader。前者用来定义一个数据集，需要实现__init__、__getitem__和__len__三个方法。__init__方法用来初始化这个数据集，__getitem__用来根据索引返回数据集中的一个数据，__len__用来返回数据集中数据的总个数。在定义好数据集之后，可以用torch.utils.data.DataLoader来对数据集进行读取。其工作原理为：torch.utils.data.DataLoader会先调用数据集的__len__获取数据集大小，之后按照其本身的参数设置，按照随机或者非随机的方式调用数据集的__getitem__方法来获取单个的数据，最后通过collate_fn来将多个数据组合成一个 batch。更多细节可以参考 PyTorch 的官方文档。

在本实训中，我们将用到 MNIST 数据集。这是计算机视觉领域的一个常用数据集，因此 PyTorch 已经内置了其实现。我们将会直接使用这个实现。如果你想了解实现的细节，可以参考官方实现进行学习。

在使用torch.utils.data.Dataset和torch.utils.data.DataLoader构建好 data loader 之后，就可以用通过迭代的方法来获取数据：

import torch
from torchvision import datasets, transforms
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
data_root = 'path/to/mnist/data'
kwargs = {'num_workers': 1, 'pin_memory': True}
dataset = datasets.MNIST(data_root, train=True, download=False, transform=transform)
train_loader = torch.utils.data.DataLoader(
    dataset, batch_size=batch_size, shuffle=True, **kwargs)
for data, target in train_loader:
    # train network code
使用PyTorch训练网络模型
在解决了数据的问题之后，下一步我们来解决模型的训练。在上一关中，我们学习了对每个torch.nn.Module，都要实现一个forward方法，并且知道torch.nn.Module是 callable 的，对其进行调用会直接调用 forward 方法。通过这些操作，可以实现网络的前向传播，即预测部分。

但是，对于网络的训练来说，还缺了很多部分。首先是损失函数。因为我们的目标是 MNIST 数据集上的分类任务，所以我们使用交叉熵，你可以通过torch.nn.CrossEntropy或者torch.nn.functional.cross_entropy来调用。在计算了 loss 之后，下一步需要进行的就是反向传播，这里可以通过对 loss 调用backward方法来实现。

然后你还需要一个优化器，我们之前学习的随机梯度下降就是一种优化器。PyTorch 提供了一系列不同的优化器，在torch.optim中，包括 SGD、Adam、AdaDelta、RMSProp 等，因为其背后的原理复杂，这里不做过多的介绍，希望了解更多的同学可以阅读这篇文章。为了方便你的实现，我们推荐使用 AdaDelta 来完成你的实训，并且设置学习率为 0.1。这里需要注意一个细节，在反向传播之前，需要调用 optimizer.zero_grad() 来清空之前 batch 计算过的梯度，防止出错。最后，调用 optimizer.step() 就可以。

在网络模型的训练过程中，学习率并不是一成不变的，通常会随着训练的进行进行衰减。这就需要使用torch.optim.lr_scheduler来对学习率进行处理。同样的，PyTorch 也提供了很多处理学习率的方法，这里我们推荐使用 StepLR，每个 epoch 学习率衰减为之前的 0.7 倍。同样的，在每个 epoch 的最后，调用 lr_scheduler.step() 就可以实现对学习率的调节。

总结一下，网络的训练分为以下步骤：

定义损失函数、优化器、学习率调节器；
载入数据，对于每个 batch，进行以下操作：
  a. 清空之前的梯度；
  b. 前向传播；
  c. 计算 loss；
  d. 反向传播；
  e. 优化器更新；
3. 每个 epoch 结束时，学习率调节器更新。

编程要求
根据提示，在右侧编辑器 Begin 和 End 之间补充代码，使用 PyTorch 实现并训练网络模型。首先，你需要重新实现一个网络模型，这个网络模型你可以自行设计，也可以采用上一关中的推荐模型。之后，你需要实现训练代码，对网络模型进行训练。

在实现训练代码时，你需要完成train函数，测试代码会根据你实现的网络模型类，创建一个网络模型实例，然后将 data loader 以及训练的总 epoch 数传入 train 函数，你需要对网络模型训练 num_epoch 个 epoch 之后返回。

测试说明
平台会对你编写的代码进行测试。我们会对你训练完成的网络模型进行测试，跑通即可通关。

开始你的任务吧，祝你成功！

说点什么
resize-icon
12345678910111213141516171819202122
from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR



测试结果
测试集1
本关最大执行时间：600秒
上一关
run
评测
