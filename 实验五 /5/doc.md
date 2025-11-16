
夏炘航
gold13260
5.2 Adaboost算法
实验总用时：00:00:01
nav
第2关：Adaboost算法
1000
学习内容
参考答案
记录
评论
任务描述
相关知识
数据集介绍
Adaboost算法原理
Adaboost算法流程
编程要求
测试说明
任务描述
本关任务：用 Python 实现 Adaboost，并通过鸢尾花数据集中鸢尾花的 2 种属性与种类对 Adaboost 模型进行训练。我们会调用你训练好的 Adaboost 模型，来对未知的鸢尾花进行分类。

相关知识
为了完成本关任务，你需要掌握：1. Adaboost 算法原理，2. Adaboost 算法流程。

数据集介绍
 

数据集为鸢尾花数据，一共有 150 个样本，每个样本有 4 个特征，由于 Adaboost 是一个串行的迭代二分类算法，运算成本较大，为了减轻运算成本，我们只利用其中两个特征与两种类别构造与训练模型，且 adaboost 算法返回的值为 1 与 -1，所以要将标签为 0 的数据改为 -1 部分数据如下图：

 

 

数据获取代码：

#获取并处理鸢尾花数据
def create_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['label'] = iris.target
    df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
    data = np.array(df.iloc[:100, [0, 1, -1]])
    #将标签为0的数据标签改为-1
    for i in range(len(data)):
        if data[i,-1] == 0:
            data[i,-1] = -1
    return data[:,:2], data[:,-1]
Adaboost算法原理
对提升方法来说，有两个问题需要回答：一是在每一轮如何改变训练数据的权值或概率分布；二是如何将弱分类器组合成一个强分类器。关于第 1 个问题，AdaBoost的做法是，提高那些被前一轮弱分类器错误分类样本的权值，而降低那些被正确分类样本的权值。这样一来，那些没有得到正确分类的数据，由于其权值的加大而受到后一轮的弱分类器的更大关注。于是，分类问题被一系列的弱分类器“分而治之”。至于第 2 个问题，即弱分类器的组合，AdaBoost采取加权多数表决的方法，加大分类误差率小的弱分类器的权值，使其在表决中起较大的作用，减小分类误差率大的弱分类器的权值，使其在表决中起较小的作用。

Adaboost算法流程
 AdaBoost 是 AdaptiveBoost 的缩写，表明该算法是具有适应性的提升算法。

算法的步骤如下：

1.给每个训练样本(x 
1
​
 ,x 
2
​
 ,..,x 
N
​
 )分配权重，初始权重w 
1
​
 均为1/N；

2.针对带有权值的样本进行训练，得到模型G 
m
​
 （初始模型为G 
1
​
 ）；

3.计算模型G 
m
​
 的误分率：

e 
m
​
 = 
i
∑
N
​
 w 
i
​
 I(y 
i
​
  

​
 =G 
M
​
 (X 
i
​
 ))

其中：

I(y 
i
​
  

​
 =G 
M
​
 (X 
i
​
 )

为指示函数，表示括号内成立时函数值为 1，否则为 0。

4.计算模型G 
m
​
 的系数：

α 
m
​
 = 
2
1
​
 log[ 
e 
m
​
 
1−e 
m
​
 
​
 ]

5.根据误分率e和当前权重向量w 
m
​
 更新权重向量：

w 
m+1,i
​
 = 
z 
m
​
 
w 
m
​
 
​
 exp(−α 
m
​
 y 
i
​
 G 
m
​
 (x 
i
​
 ))

其中Z 
m
​
 为规范化因子：

z 
m
​
 = 
i=1
∑
m
​
 w 
mi
​
 exp(−α 
m
​
 y 
i
​
 G 
m
​
 (x 
i
​
 ))

6.计算组合模型f(x)=∑ 
m=1
M
​
 α 
m
​
 G 
m
​
 (x 
i
​
 )的误分率；

7.当组合模型的误分率或迭代次数低于一定阈值，停止迭代；否则，回到步骤 2。

编程要求
根据提示，在右侧编辑器的 begin-end 间补充 Python 代码，实现 Adaboost 算法，并利用训练好的模型对鸢尾花数据进行分类。

测试说明
只需返回分类结果即可，程序内部会检测您的代码，预测正确率高于 95% 视为过关。

开始你的任务吧，祝你成功！

说点什么
resize-icon
1234567891011121314151617181920212223
#encoding=utf8
import numpy as np
#adaboost算法
class AdaBoost:
    '''
    input:n_estimators(int):迭代轮数
          learning_rate(float):弱分类器权重缩减系数
    '''
    def __init__(self, n_estimators=50, learning_rate=1.0):
        self.clf_num = n_estimators

测试结果
测试集1
本关最大执行时间：20秒
上一关
下一关
run
评测
