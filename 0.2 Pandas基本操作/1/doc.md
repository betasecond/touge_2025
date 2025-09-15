：数组创建
100
学习内容
参考答案
记录
评论
任务描述
相关知识
编程要求
测试说明
任务描述
本关的小目标是，使用 Numpy 创建一个多维数组。

相关知识
在 Python 中创建数组有许多的方法，这里我们使用 Numpy 中的arange方法快速的新建一个数组：

import numpy as np
a = np.arange(5)
其中import numpy as np是指引入Numpy这个库，并取别名为np。之所以取别名，是为了代码编写的方便。a=np.arange(5)是指将数值0 1 2 3 4赋值给a这个变量，这样我们就快速的创建了一个一维数组。

创建多维数组的方法是:

import numpy as np
b = np.array([np.arange(6),np.arange(6)])
这里，我们使用两个arange方法，创建了两个1x6的一维数组，然后使用numpy的array方法，将两个一维数组组合成一个2x6的二维数组。从而达到了创建多维数组的目的。

numpy创建的数组可以直接复制，具体代码示例如下：

import numpy as np
x = [y for y in range(6)]
b=np.array([x]*4)
该段代码会创建一个4*6的数组。

编程要求
本关的任务是，补全右侧编辑器中 Begin-End 区间的代码，以实现创建一个m*n的多维数组的功能。具体要求如下：

函数接受两个参数，然后创建与之对应的的多维数组；

本关的测试样例参见下文。

本关设计的代码文件cnmda.py的代码框架如下：

# 引入numpy库
import numpy as np
# 定义cnmda函数
def cnmda(m,n):
'''
创建numpy数组
参数：
m:第一维的长度
n: 第二维的长度
返回值:
ret: 一个numpy数组
'''
ret = 0

    # 请在此添加创建多维数组的代码并赋值给ret
    #********** Begin *********#
    #********** End **********#
    
    return ret
测试说明
本关的测试过程如下:

平台运行step1/cnmdatest.py文件，并以标准输入方式提供测试输入；

cnmdatest.py文件调用cnmda中的cnmda方法，平台获取cnmdatest.py的输出，然后将其与预期输出作对比，如果一致，则测试通过；否则测试失败。

以下是平台对step1/cnmdatest.py的测试样例：

测试输入： 5 8

预期输出： (5,8)

测试输入： 4 9

预期输出： (4,9)

开始你的任务吧，祝你成功!