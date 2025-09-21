任务描述
相关知识
读取CSV
查看后n行
查看总行数
修改列名
编程要求
测试说明
任务描述
本关任务：根据编程要求，完成相关代码的编写。

相关知识
在使用机器学习工具包对数据进行修改、探索和分析之前，我们必须先讲外部数据导入。使用Pandas导入数据比Numpy要容易。在这里我们将使用英国降雨数据，数据已下好并放在本实训的当前文件夹。

读取CSV
# Reading a csv into Pandas.
# 如果数据集中有中文的话，最好在里面加上 encoding = 'gbk' ，以避免乱码问题。后面的导出数据的时候也一样。
df = pd.read_csv('uk_rain_2014.csv', header=0)
这里我们从csv文件里导入了数据，并储存在DataFrame中。这一步非常简单，你只需要调用read_csv然后将文件的路径传进去就行了。header 关键字告诉Pandas哪些是数据的列名。如果没有列名的话就将它设定为 None。
数据导入pandas之后，我们该怎么查看数据呢？
#####查看前n行
# Getting first x rows.
df.head(5)

查看后n行
# Getting last x rows.
df.tail(5)
查看总行数
# Finding out how many rows dataset has.
len(df)
修改列名
我们通常使用列的名字来在Pandas中查找列。这一点很好而且易于使用，但是有时列名太长，我们需要缩短列名。
# Changing column labels.
df.columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']

编程要求
根据提示，在右侧编辑器begin-end处补充代码：

将test3/uk_rain_2014.csv中的数据导入到df1中；

将列名修改为['water_year','rain_octsep','outflow_octsep','rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']；

计算df1的总行数并存储在length1中。

测试说明
如果答案正确，则会输出True。

开始你的任务吧，祝你成功！


