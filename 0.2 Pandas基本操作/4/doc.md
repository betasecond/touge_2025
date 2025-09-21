任务描述
相关知识
什么是Pandas
Pandas数据结构
Pandas读取数据
常用的pands数据读写接口：
从.csv文件中读取数据
将数据写入到.csv文件中
编码规范：
附：常用的读写参考表
编程要求
测试说明
任务描述
本关任务：编写Python代码，使用Pandas读取和写入内容。

相关知识
为了完成本关任务，你需要掌握：

什么是Pandas
Pandas数据结构
Pandas读取数据
Pandas写入数据
什么是Pandas
Pandas 是Python的核心数据分析支持库，提供了快速、灵活、明确的数据结构，旨在简单、直观地处理关系型、标记型数据。Pandas 的目标是成为 Python 数据分析实践与实战的必备高级工具，其长远目标是成为最强大、最灵活、可以支持任何语言的开源数据分析工具。

Pandas 适用于处理以下类型的数据：

与 SQL 或 Excel 表类似的，含异构列的表格数据;
有序和无序（非固定频率）的时间序列数据;
带行列标签的矩阵数据，包括同构或异构型数据;
任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。
Pandas数据结构
Series是带标签的一维数组，可存储整数、浮点数、字符串、Python 对象等类型的数据。轴标签统称为索引。

DataFrame是由多种类型的列构成的二维标签数据结构，类似于 Excel 、SQL 表，或 Series 对象构成的字典。

维数	名称	描述
1	Series	带标签的一维同构数组
2	DataFrame	带标签的，大小可变的，二维异构表格
Pandas读取数据
常用的pands数据读写接口：
读写接口	功能
pd.read_csv()	从.csv文件中读取数据
DataFrame.to_csv()	将数据写入到.csv文件中
pd.read_excel()	从.excel文件中读取数据
DataFrame.to_excel()	将数据写入到.excel文件中
从.csv文件中读取数据
pd.read_csv()可以用来读取csv文件：

pandas.read_csv(filepath_or_buffer, sep=<object object>, delimiter=None, names=None, index_col=None, usecols=None,encoding=None)
常用参数解析：

filepath_or_buffer：设置需要访问的文件的有效路径。
sep：str, default ','，指定读取文件的分隔符.支持自定义分隔符。
delimiter：str, default None，定界符.备选分隔符（如果指定该参数，则sep参数失效）。
header：str, default None，指定作为整个数据集列名的行.如果数据集中没有列名，则需要设置header=None.对有表头的数据识别第一行作为header。
names ：array-like, default None，用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None。
index_col：int or sequence or False, default None，指定数据集中的某1列作为索引(index_col = 1/2)。
usecols：array-like, default None，指定只读取文件中的某一列数据.例如：只读取前四列，usecols = [0,1,2,3])。
squeeze：boolean, default False，如果文件值包含一列，则返回一个Series。
>>> df = pd.read_csv('data.csv', encoding='gbk', names=['第一列', '第二列', '第三列', '第四列'])
>>> df
第一列 第二列 第三列 第四列
0 姓名 语文 数学 英语
1 陈一 89 90 67
2 赵二 70 78 90
3 张三 87 86 79
4 李四 90 69 84
5 王五 78 80 69
将数据写入到.csv文件中
DataFrame.to_csv(path_or_buf=None, sep=', ', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression=None, quoting=None, quotechar='"', line_terminator='\n', chunksize=None, tupleize_cols=None, date_format=None, doublequote=True, escapechar=None, decimal='.')
常用参数解析：

path_or_buf=None： 字符串或文件句柄，默认无文件，路径或对象，如果没有提供，结果将返回为字符串。
sep : 默认字符","，输出文件的字段分隔符。
na_rep : 字符串，默认为 ‘’, 浮点数格式字符串。
float_format : 字符串，默认为 None，浮点数格式字符串。
columns : 顺序，可选列写入。
header : 字符串或布尔列表，默认为true，写出列名。如果给定字符串列表，则假定为列名的别名。
index : 布尔值，默认为Ture，写入行名称（索引）
index_label : 字符串或序列，或False,默认为None，如果需要，可以使用索引列的列标签。如果没有给出，且标题和索引为True，则使用索引名称。如果数据文件使用多索引，则应该使用这个序列。如果值为False，不打印索引字段。在R中使用index_label=False 更容易导入索引.
encoding : 编码：字符串，可选，表示在输出文件中使用的编码的字符串，Python 2上默认为“ASCII”和Python 3上默认为“UTF-8”。
>>> df.to_csv('data.csv', encoding='gbk', sep=',') # 以gbk编码保存并使用','号分隔数据。
文件内容：
第一列,第二列,第三列,第四列
0,姓名,语文,数学,英语
1,陈一,89,90,67
2,赵二,70,78,90
3,张三,87 86,79
4,李四,90,69,84
5,王五,78,80,69
编码规范：
在不同格式的编码文件中，如果不指定encoding则会出现异常。例如使用utf-8编码打开gbk编码的文件将出现下面的异常：

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd0 in position 0: invalid continuation byte
附：常用的读写参考表
Format Type	Data Description	Reader	Writer
text	CSV	read_csv	to_csv
text	JSON	read_json	to_json
text	HTML	read_html	to_html
text	Local clipboard	read_clipboard	to_clipboard
binary	MS Excel	read_excel	to_excel
binary	Python Pickle Format	read_pickle	to_pickle
SQL	SQL	read_sql	to_sql
编程要求
根据提示，在右侧编辑器的Begin-End段补充代码

任务说明：

实现使用Pandas读取gbk编码文件中的数据，并将数据写入到utf-8编码的文件中。

测试说明
只需补充代码即可，平台会对你生成的文件进行测试。

预期输出：生成的文件中的内容。

开始你的任务吧，祝你成功！