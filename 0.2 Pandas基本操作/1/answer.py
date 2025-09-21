import pandas as pd
import numpy as np # 导入 numpy 库以使用 np.nan

########## Begin ##########

# 1. 使用字典定义数据。字典的键是列名，值是包含列数据的列表。
#    对于缺失值，我们使用 np.nan。
data = {
    'A': [90, 89, 78],
    'B': [82, 95, 92],
    'C': [78.0, 67.0, np.nan],
    'D': [78.0, 67.0, np.nan]
}

# 2. 使用 pd.DataFrame() 函数创建 DataFrame。
#    第一个参数是数据，第二个参数 `index` 用于指定行标签。
df1 = pd.DataFrame(data, index=['a', 'b', 'c'])

########## End ##########

# 打印最终的 DataFrame
print(df1)
