#encoding=utf8 
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. 获取训练数据
train_data = pd.read_csv('./step3/train_data.csv')

# 2. 获取训练标签
# 加载CSV
train_label_df = pd.read_csv('./step3/train_label.csv')
# 提取 'target' 列作为训练标签
train_label = train_label_df['target']

# 3. 获取测试数据
test_data = pd.read_csv('./step3/test_data.csv')

# 4. 初始化线性回归模型
# 使用默认参数 (fit_intercept=True)
lr = LinearRegression()

# 5. 训练模型
lr.fit(train_data, train_label)

# 6. 对测试集进行预测
predictions = lr.predict(test_data)

# 7. 将预测结果保存到 ./step3/result.csv
# 将Numpy数组格式的预测结果转换为Pandas DataFrame，并指定列名为 'result'
result_df = pd.DataFrame(predictions, columns=['result'])

# 保存为CSV文件，index=False 表示不保存行索引，符合题目要求
result_df.to_csv('./step3/result.csv', index=False)
