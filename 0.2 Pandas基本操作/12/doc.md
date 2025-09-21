任务描述
相关知识
duplicated()
drop_duplicates()
编程要求
测试说明
任务描述
本关任务：根据编程要求，完成相关代码的编写。

相关知识
duplicated()
DataFrame的duplicated方法返回一个布尔型Series，表示各行是否是重复行。具体用法如下：

In[1]: df = DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[1,1,2,3,3,4,4]})
In[2]: df
Out[2]:
k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
In[3]: df.duplicated()
Out[3]:
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
drop_duplicates()
drop_duplicates()用于去除重复的行数，具体用法如下：

In[4]: df.drop_duplicates()
Out[4]:
k1  k2
0  one   1
2  one   2
3  two   3
5  two   4
编程要求
根据提示，在右侧编辑器Begin-End处补充代码:

去除df1中重复的行，并把结果保存到df2中。
测试说明
如果答案正确，则会输出True。

开始你的任务吧，祝你成功！