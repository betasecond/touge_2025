任务描述
相关知识
按行排序
按值排序
编程要求
测试说明
任务描述
本关任务：根据编程要求，完成相关代码的编写。

相关知识
本关我们将学习处理Series和DataFrame中的数据的基本手段，我们将会探讨Pandas最为重要的一些功能。
#####对索引进行排序
Series用sort_index()按索引排序，sort_values()按值排序；
DataFrame也是用sort_index()和sort_values()。

In[73]: obj = Series(range(4), index=['d','a','b','c'])
In[74]: obj.sort_index()  
Out[74]:
a    1
b    2
c    3
d    0
dtype: int64
In[78]: frame = DataFrame(np.arange(8).reshape((2,4)),index=['three', 'one'],columns=['d','a','b','c'])
In[79]: frame
Out[79]:
d  a  b  c
three  0  1  2  3
one    4  5  6  7
In[86]: frame.sort_index()
Out[86]:
d  a  b  c
one    4  5  6  7
three  0  1  2  3
按行排序
In[89]: frame.sort_index(axis=1, ascending=False)
Out[89]:
d  c  b  a
three  0  3  2  1
one    4  7  6  5
按值排序
Series:

In[92]: obj = Series([4, 7, -3, 2])
In[94]: obj.sort_values()
Out[94]:
2   -3
3    2
0    4
1    7
dtype: int64
DataFrame:

In[95]: frame = DataFrame({'b':[4, 7, -3, 2], 'a':[0, 1, 0, 1]})
In[97]: frame.sort_values(by='b')  #DataFrame必须传一个by参数表示要排序的列
Out[97]:
a  b
2  0 -3
3  1  2
0  0  4
1  1  7
编程要求
根据提示，在右侧编辑器Begin-End处补充代码：

对代码中s1进行按索引排序，并将结果存储到s2；

对代码中d1进行按值排序（index为f），并将结果存储到d2。

测试说明
如果答案正确，则会输出True。

开始你的任务吧，祝你成功！