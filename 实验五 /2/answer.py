
import numpy as np

#建议代码，也算是Begin-End中的一部分
from collections import  Counter
from sklearn.tree import DecisionTreeClassifier

class RandomForestClassifier():
    def __init__(self, n_model=10):
        '''
        初始化函数
        '''
        #分类器的数量，默认为10
        self.n_model = n_model
        #用于保存模型的列表，训练好分类器后将对象append进去即可
        self.models = []
        #用于保存决策树训练时随机选取的列的索引
        self.col_indexs = []


    def fit(self, feature, label):
        '''
        训练模型
        :param feature: 训练集数据，类型为ndarray
        :param label: 训练集标签，类型为ndarray
        :return: None
        '''

        #************* Begin ************#

        # 获取样本数量和特征数量
        n_samples, n_features = feature.shape

        # 计算每棵树随机选择的特征数量：k = log2(特征数量)
        k = int(np.log2(n_features))
        if k < 1:
            k = 1

        # 训练n_model棵决策树
        for i in range(self.n_model):
            # 1. 随机有放回采样（Bootstrap）
            indices = np.random.choice(n_samples, size=n_samples, replace=True)
            sample_feature = feature[indices]
            sample_label = label[indices]

            # 2. 随机选择k个特征
            col_index = np.random.choice(n_features, size=k, replace=False)
            col_index = sorted(col_index)  # 排序方便后续使用
            self.col_indexs.append(col_index)

            # 3. 根据选择的特征索引获取训练子集
            sub_feature = sample_feature[:, col_index]

            # 4. 创建并训练决策树
            model = DecisionTreeClassifier()
            model.fit(sub_feature, sample_label)

            # 5. 保存模型
            self.models.append(model)

        #************* End **************#


    def predict(self, feature):
        '''
        :param feature:测试集数据，类型为ndarray
        :return:预测结果，类型为ndarray，如np.array([0, 1, 2, 2, 1, 0])
        '''
        #************* Begin ************#

        # 收集所有模型的预测结果
        predictions = []

        # 对每个模型进行预测
        for i, model in enumerate(self.models):
            # 获取该模型训练时使用的特征索引
            col_index = self.col_indexs[i]
            # 使用相同的特征进行预测
            sub_feature = feature[:, col_index]
            pred = model.predict(sub_feature)
            predictions.append(pred)

        # 转换为数组
        predictions = np.array(predictions)

        # 对每个样本进行投票
        result = []
        for i in range(len(feature)):
            votes = predictions[:, i]
            # 使用Counter统计，选择票数最多的类别
            most_common_label = Counter(votes).most_common(1)[0][0]
            result.append(most_common_label)

        return np.array(result)

        #************* End **************#
