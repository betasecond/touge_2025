任务描述
相关知识
创建多级索引
多级索引的取值与切片
编程要求
任务描述
本关任务：根据相关知识以及编程要求，得到目标DataFrame多级索引。

相关知识
创建多级索引
通过MultiIndex构建多级索引：

index = [('California', 2000), ('California', 2010), ('New York', 2000), ('New York', 2010), ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956, 18976457, 19378102, 20851820, 25145561]
pop = pd.Series(populations, index=index)
# 1.基于元组创建
index1 = pd.MultiIndex.from_tuples(index)
index1
Out：
MultiIndex(levels=[['California', 'New York', 'Texas'], [2000, 2010]], codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]])
MultiIndex里面有一个levels属性表示索引的等级——这样做可以将州名和年份作为每个数据点的不同标签。如果将前面创建的pop的索引重置（reindex）为MultiIndex，就会看到层级索引。其中前两列表示Series的多级索引值，第三列式数据。

pop1 = pop.reindex(index1)
pop1
Out：
California 2000 33871648
2010 37253956
New York   2000 18976457
2010 19378102
Texas      2000 20851820
2010 25145561
dtype: int64
查询2010年的数据。

pop[:, 2010]  # 得到的是一个单索引数组
Out：
California 37253956
New York   19378102
Texas      25145561
dtype: int64
以上的例子都是Series创建多级行索引，而每个DataFrame的行与列都是对称的，也就是说既然有多级行索引，那么同样可以有多级列索引。只需要在创建DataFrame时将columns的参数传入一个MultiIndex。

通过二维索引数组创建多级索引：
Series或DataFrame创建多级索引最直接的办法就是将index参数设置为至少二维的索引数组。

df = pd.DataFrame(np.random.rand(4, 2), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=['data1', 'data2'])
df
Out:
data1    data2
a 1 0.554233 0.356072
2 0.925244 0.219474
b 1 0.441759 0.610054
2 0.171495 0.886688
MultiIndex的创建工作将在后台完成。同理，如果你把将元组作为键的字典传递给Pandas，Pandas也会默认转换为MultiIndex。

显示的创建多级索引：
你可以用pd.MultiIndex中的类方法更加灵活地构建多级索引。

# 有不同等级的若干简单数组组成的列表来构建
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
# 包含多个索引值的元组构成的列表创建
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
# 由两个索引的笛卡尔积（Cartesian product）创建
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])
# 三种创建方法的结果都一致
Out:
MultiIndex(levels=[['a', 'b'], [1, 2]],
codes=[[0, 0, 1, 1], [0, 1, 0, 1]])
在创建Series或DataFrame时，可以将这些对象作为index参数，或者通过reindex方法更新Series或DataFrame的索引。

多级索引的等级名称
你可以在前面任何一个MultiIndex构造器中通过names参数设置等级名称，也可以在创建之后通过索引的names属性来修改名称。

pop.index.names = ['state', 'year']
Out:
state      year
California 2000 33871648
2010 37253956
New York   2000 18976457
2010 19378102
Texas      2000 20851820
2010 25145561
dtype: int64
多级列索引
每个DataFrame的行与列都是对称的，也就是说既然有多级行索引，那么同样可以有多级列索引。

多级索引与DataFrame的相互转换
unstack()方法可以快速将一个多级索引的Series转化为普通索引的DataFrame。

pop.unstack()   # stack()可以将DataFrame转换为多级索引
Out：
2000     2010
California 33871648 37253956
New York   18976457 19378102
Texas      20851820 25145561
多级索引的取值与切片
Series多级索引；
以各州历年人口数量创建的多级索引Series为例：

pop
Out:     
state      year
California 2000 33871648
2010 37253956
New York   2000 18976457
2010 19378102
Texas      2000 20851820
2010 25145561
dtype: int64
获取单个元素：

pop['California',2000]
Out：
33871648
MultiIndex也支持局部取值（partial indexing），即只取索引的某一个层级。假如只取最高级的索引，获得的结果是一个新的Series，未被选中的低层索引值会被保留：

pop['California']
Out：
year
2000 33871648
2010 37253956
dtype: int640
其他取值与数据选择的方法（详情请参考该实训）也都起作用。

DataFrame多级索引：

index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
# 模拟数据
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
# 创建一个包含多级列索引的DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data
Out：
subject     Bob      Guido     Sue
type        HR  Temp  HR  Temp  HR  Temp
year  visit
2013  1     31.0 38.7 32.0 36.7 35.0 37.2
2 44. 0     37.7 50.0 35.0 29.0 36.7
2014  1     30.0 37.4 39.0 37.8 61.0 36.9
2 47. 0     37.8 48.0 37.3 51.0 36.5
由于DataFrame的基本索引是列索引，因此Series中多级索引的用法到了DataFrame中就应用在列上了。

health_data['Guido', 'HR']
Out：
year visit
2013 1         32.0
2         50.0
2014 1         39.0
2         48.0
Name: (Guido, HR), dtype: float64
loc、iloc、ix三个索引器都可以使用，虽然这些索引器将多维数据当作二维数据处理，但是在loc和iloc中可以传递多个层级的索引元组。

health_data.loc[:, ('Bob', 'HR')]
Out：
year visit
2013  1 31.0
2 44.0
2014  1 30.0
2 47.0
Name: (Bob, HR), dtype: float64
这种索引元组的用法不是很方便，如果在元组中使用切片还会导致语法错误。

health_data.loc[(:, 1), (:, 'HR')]
# 这种切片方式会报错
Pandas的IndexSlice对象可以解决上述问题。

idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]
Out：
subject     Bob  Guido Sue
type        HR   HR    HR
year visit
2013 1      31.0 32.0  35.0
2014 1      30.0 39.0  61.0
编程要求
本关的编程任务是补全右侧上部代码编辑区内的相应代码，要求实现如下功能：

使用MultiIndex创建如下DataFrame多级索引：




然后通过转置、stack()方法得到以下数据：




最后通过取值和切片得到目标数据：



具体要求请参见后续测试样例。
请先仔细阅读右侧上部代码编辑区内给出的代码框架，再开始你的编程工作！
####测试说明
平台会对你编写的代码进行测试，对比你输出的数值与实际正确的数值，只有所有数据全部计算正确才能进入下一关。

测试输入：

无测试输入

平台会对你编写的代码进行测试：

预期输出：




开始你的任务吧，祝你成功！