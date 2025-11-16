#********* Begin *********#

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. 读取训练数据和标签
# 注意：as_matrix()在新版pandas中已弃用，改用values
train_data = pd.read_csv('./step7/train_data.csv').values
train_label = pd.read_csv('./step7/train_label.csv').values

# 2. 读取测试数据
test_data = pd.read_csv('./step7/test_data.csv').values

# 3. 创建决策树分类器
# 使用gini系数作为划分标准
clf = DecisionTreeClassifier()

# 4. 训练模型
# train_label需要展平为一维数组
clf.fit(train_data, train_label.ravel())

# 5. 预测测试集
predict_result = clf.predict(test_data)

# 6. 将预测结果保存到CSV文件
# 需要转换为DataFrame格式，保持与标签文件格式一致
predict_df = pd.DataFrame(predict_result)
predict_df.to_csv('./step7/predict.csv', index=False)

#********* End *********#