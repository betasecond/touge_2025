任务描述
相关知识
编程要求
测试说明
任务描述
本关任务：根据编程要求，完成相关代码的编写。

相关知识
DataFrame是一个表格型的数据结构，是以一个或多个二维块存放的数据表格（层次化索引），DataFrame既有行索引还有列索引，它有一组有序的列，每列既可以是不同类型（数值、字符串、布尔型）的数据，或者可以看做由Series组成的字典。
DataFrame创建:
dictionary = {'state':['0hio','0hio','0hio','Nevada','Nevada'],
'year':[2000,2001,2002,2001,2002],
'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(dictionary)
修改行名：
frame=DataFrame(dictionary,index=['one','two','three','four','five'])
添加修改：
frame['add']=[0,0,0,0,0]
添加Series类型：
value = Series([1,3,1,4,6,8],index = [0,1,2,3,4,5])
frame['add1'] = value

编程要求
根据提示，在右侧编辑器begin-end处补充代码：

创建一个五行三列的名为df1的DataFrame数组，列名为 [states,years,pops]，行名['one','two','three','four','five']；

给df1添加新列，列名为new_add，值为[7,4,5,8,2]。

测试说明
如果答案正确，则会输出True。

开始你的任务吧，祝你成功！

