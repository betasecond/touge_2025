任务描述
相关知识
Pandas中的数据结构
了解Series
编程要求
测试说明
任务描述
本关任务：仔细阅读编程要求，完成相关要求。

相关知识
Pandas是为了解决数据分析任务而创建的，纳入了大量的库和标准数据模型，提供了高效地操作大型数据集所需的工具。
对于Pandas包，在Python中常见的导入方法如下：

from pandas import Series,DataFrame
import pandas as pd
Pandas中的数据结构
Series: 一维数组，类似于Python中的基本数据结构list，区别是Series只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。就像数据库中的列数据；
DataFrame: 二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器；
Panel：三维的数组，可以理解为DataFrame的容器。
了解Series
为了开始使用Pandas，我们必需熟悉它的两个重要的数据结构：Series 和DataFrame。虽然它们不是每一个问题的通用解决方案，但可以提供一个坚实的，易于使用的大多数应用程序的基础。
Series是一个一维的类似的数组对象，包含一个数组的数据（任何NumPy的数据类型）和一个与数组关联的数据标签，被叫做索引 。最简单的Series是由一个数组的数据构成：

In [1]:obj=Series([4,7,-5,3])
In [2]:obj
Out[2]:
0 4
1 7
2 -5
3 3
Series的交互式显示的字符串表示形式是索引在左边，值在右边。因为我们没有给数据指定索引，一个包含整数0到N-1这里N是数据的长度）的默认索引被创建。你可以分别的通过它的values和index属性来获取 Series的数组表示和索引对象：

In [3]: obj.values
Out[3]:array([4,7,-5,3])
In [4]: obj.index
Out[4]:Int64Index([0,1,2,3])
通常，需要创建一个带有索引来确定每一个数据点的Series。

In [5]:obj2=Series([4,7,-5,3],index=['d','b','a','c'])
In [6]:obj2
Out[6]:
d 4
b 7
a -5
c 3
如果你有一些数据在一个Python字典中，你可以通过传递字典来从这些数据创建一个Series，只传递一个字典的时候，结果Series中的索引将是排序后的字典的键。

In [7]:sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
In [8]:obj3=Series(sdata)
In [9]:obj3
Out[9]:
Ohio   35000
Texas  71000
Oregon 16000
Utah   5000
编程要求
根据提示，在右侧编辑器Begin-End处补充代码：

创建一个名为series_a的series数组，当中值为[1,2,5,7],对应的索引为['nu', 'li', 'xue', 'xi']；

创建一个名为dict_a的字典，字典中包含如下内容{'ting':1, 'shuo':2, 'du':32, 'xie':44}；

将dict_a字典转化成名为series_b的series数组。

测试说明
如果答案正确，则会输出True。
开始你的任务吧，祝你成功！