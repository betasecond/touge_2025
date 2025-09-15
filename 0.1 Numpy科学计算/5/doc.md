第5关：文件读写
100
学习内容
参考答案
记录
评论
任务描述
相关知识
NumPy 读写文本格式的数据
NumPy 读写二进制文件
编程要求
测试说明
任务描述
本关任务：根据任务要求使用 Numpy 进行文件读写。

相关知识
通常情况下，数据是以文件形式存储的。常用的存储文件的格式有文本文件、CSV 格式文件和二进制格式文件等。在数据分析中，经常需要从文件中读取数据或将数据写入文件，因此，学会读写文件操作是深入学习 NumPy 的基础。下面将分别介绍如何使用 NumPy 函数来读写一维或二维数组的文本文件、CSV 格式文件、二进制格式文件和多维数据文件。

Numpy中常用的文件处理方法：

函数名
numpy.savetxt()	将数据以文本格式保存到文件中
numpy.loadtxt()	读取文本格式的数据
numpy.genfromtxt()	读取文本格式的数据
numpy.save()	将数据以二进制形式保存到文件中
numpy.load()	读取二进制文件中的数据
NumPy 读写文本格式的数据
使用 savetxt() 方法将数据以文本格式保存到文件中

savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
函数中参数说明如下：

fname：文件名或者文件句柄。如果文件名以".gz"结尾，则该文件会被自动以 gzip 形式压缩。当然，"loadtxt"也可以解析被压缩的文件。
X：一维或者二维数组。需要写入文本文件的数据。
fmt：str 或者 str 序列，可选参数。单一格式(%10.5f)，序列格式或多重格式字符串，例如。“Iteration %d—%10.5f”，在这种情况下“delimiter”参数被忽略。
delimiter：str，可选参数。用于分隔列的字符串或者字符。
newline：str，可选参数。用于分隔行的字符串或者字符。
header：str，可选参数。将被添加到文件开头的字符串。
footer：str，可选参数。将被添加到文件结尾的字符串。
comments：str，可选参数。将作为前缀被添加到"header" 和 "footer"的字符串，用于将这部分标记为注释内容。默认是"#"。
encoding：{None, str}, 可选参数。用于对输出文件的编码。不适用与输出流。如果编码格式不是"bytes" 或者"latin1"，那么将无法正常 load。
使用loadtxt()方法读取文本格式的数据：

loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0, encoding='bytes')
函数中参数说明如下：

fname：文件，str 或者是 pathlib.Path。
dtype：返回的数据类型，默认 float。
comments：str，可选参数。注释说明。默认是"#"。
delimiter：str，可选参数。数值的分隔符，默认是空格。
skiprows：int，可选参数。跳过的行数，默认是0。
usecols：int或者序列，可选参数。读取的列数，0为起点。例如，当usecols=（1,4,5），读取第2列，第5列和第6列。默认值是读取所有列。
unpack：bool 型，可选参数。若为为 True，可以将数据进行拆分，例如 x, y, z = loadtxt(...)。默认值是 False。
encoding: 用于对输入文件的解码。
注意：文件中的每一行数据的数量需要相同。

NumPy 读写二进制文件
在 NumPy 中，load() 和 save() 函数是专门用于读写二进制格式文件的，它们具有自动处理数组元素类型和形状的功能。savez() 函数能提供将多个数组存储至一个文件的能力，save() 函数保存之后后缀名为 npy，savez() 函数保存之后后缀名 .npz。

使用解压程序打开 npz 文件可以看到里面是若干个以“数组名称”命名的 NPY 格式的文件，数组名称默认为“arr_数字”的形式，在 savez() 函数中可以通过指明函数的参数名称来命名数组。

使用 save() 或 savez() 函数写二进制格式文件

numpy.save(file, arr, allow_pickle=True, fix_imports=True)
函数中参数说明如下：

file：文件或 str，保存数据的文件或文件名。如果 file是一个文件对象，则文件名不变。如果 file 是一个字符串，则.npy扩展名将附加到文件名后面，如果它还没有；
allow_pickle：bool，可选，允许使用 Python pickles 保存对象数组。禁止 pickles 的原因包括安全性（加载 pickled 数据可以执行任意代码）和可移植性（ pickled 对象可能无法在不同的 Python 安装上加载，例如，如果存储的对象需要不可用的库，并且并非所有 pickled 数据都兼容 Python 2 和 Python 3 ）。默认值：True；
fix_imports：bool，可选，只有在强制 Python 3 中的对象数组中的对象以 Python 2 兼容的方式被 pickle 时才有用。如果 fix_imports 为 True，pickle 将尝试将新的 Python 3 名称映射到 Python 2 中使用的旧模块名称，以便使用 Python 2 可读取 pickle 数据流；
arr：array_like，要保存的数组数据。
将多个数组以未压缩的.npz格式保存到单个文件中。

numpy.savez(file, *args, **kwds)
函数中参数说明如下：

file：str 或文件要保存数据的文件名（字符串）或打开文件（类文件对象）。如果 file 是一个字符串，则.npz扩展名将附加到文件名之后（如果尚未存在）。
args：参数，可选，数组保存到文件。由于 Python 不可能知道savez之外的数组的名称，因此数组将以名称“arr_0”，“arr_1”等保存。这些参数可以是任何表达式。
kwds：关键字参数，可选，数组保存到文件。数组将保存在带有关键字名称的文件中。
使用 load() 函数读取二进制格式文件

load() 函数的格式如下：

numpy.load(file, mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII')
函数中参数说明如下：

file：类文件对象或字符串，要读取的文件。类文件对象必须支持seek()和read()方法。Pickled 文件要求文件样对象也支持readline()方法。
mmap_mode：{None，'r +'，'r'，'w +'，'c'}，可选，如果不是 None，那么使用给定的模式对内存映射文件（有关模式的详细描述，请参阅numpy.memmap）。内存映射数组保存在磁盘上。但是，它可以像任何ndarray访问和切片。内存映射对于访问大文件的小片段而不将整个文件读入内存特别有用。
allow_pickle：bool，可选，允许加载 pickled 对象数组存储在 npy 文件中。禁止 pickles 的原因包括安全性，因为加载 pickled 数据可以执行任意代码。如果不允，加载对象数组将失败。默认值：True
fix_imports：bool，可选，仅当在 Python 3 上加载 Python 2 生成的 pickled 文件时有用，其中包括包含对象数组的 npy / npz 文件。如果 fix_imports 为 True，pickle 将尝试将旧的 Python 2 名称映射到 Python 3 中使用的新名称。
encoding：str，可选，读取 Python 2 字符串时使用的编码。仅当在 Python 3 上加载 Python 2 生成的 pickled 文件时有用，其中包括包含对象数组的 npy / npz 文件。不允许使用“latin1”，“ASCII”和“bytes”以外的值，因为它们可能损坏数值数据。默认值：'ASCII'
编程要求
根据任务提示，在右侧编辑器 Begin-End 部分补充代码。

任务要求：

从指定路径的二进制文件中（"step5/FileHandling/files/A.npy"）读取 NumPy 矢量数组 A ，从从指定路径的 txt 文件中读取矢量数组 B （"step5/FileHandling/files/B.txt"），然后使用通用函数 numpy.add() 对数组 A 和 B 进行求和，将结果保存到指定的二进制文件中（"step5/FileHandling/files/out.npy"）。
测试说明
平台会对你编写的代码和生成的文件进行测试，==请严格按照指定路径进行文件读写==：

测试输入：（"step5/FileHandling/files/A.npy"）和（"step5/FileHandling/files/B.txt"）中的数据
预期输出：（"step5/FileHandling/files/out.npy"）

判例程序将检测文件输出情况。

开始你的任务吧，祝你成功！