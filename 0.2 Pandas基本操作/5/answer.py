# 引入numpy库
import numpy as np

def task():
    """
    读取两个文件中的数组，相加后写入新文件。
    """
    # 定义文件路径
    file_a_path = "step5/FileHandling/files/A.npy"
    file_b_path = "step5/FileHandling/files/B.txt"
    output_path = "step5/FileHandling/files/out.npy"

    # 请在此处开始编写代码
    # ********** Begin **********

    # 1. 从二进制文件 A.npy 中读取数组 A
    A = np.load(file_a_path)

    # 2. 从文本文件 B.txt 中读取数组 B, 假定分隔符为逗号
    B = np.loadtxt(file_b_path, delimiter=',')

    # 3. 使用 numpy.add() 对数组 A 和 B 进行求和
    result = np.add(A, B)

    # 4. 将结果保存到二进制文件 out.npy
    np.save(output_path, result)

    # ********** End **********

# 在平台测试时，通常会自动调用需要的函数。

