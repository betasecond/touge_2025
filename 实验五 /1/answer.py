
import numpy as np
from collections import Counter
from sklearn.tree import DecisionTreeClassifier

class BaggingClassifier():
    def __init__(self, n_model=10):
        '''
        初始化函数
        '''
        #分类器的数量，默认为10
        self.n_model = n_model
        #用于保存模型的列表，训练好分类器后将对象append进去即可
        self.models = []


    def fit(self, feature, label):
        '''
        训练模型，请记得将模型保存至self.models
        :param feature: 训练集数据，类型为ndarray
        :param label: 训练集标签，类型为ndarray
        :return: None
        '''

        #************* Begin ************#

        # 获取样本数量
        n_samples = len(feature)

        # 训练n_model个分类器
        for i in range(self.n_model):
            # 1. 随机有放回采样（Bootstrap）
            # 从0到n_samples-1中随机采样n_samples个索引（可重复）
            indices = np.random.choice(n_samples, size=n_samples, replace=True)

            # 2. 根据索引获取采样数据集
            sample_feature = feature[indices]
            sample_label = label[indices]

            # 3. 创建并训练决策树分类器
            model = DecisionTreeClassifier()
            model.fit(sample_feature, sample_label)

            # 4. 将训练好的模型保存到列表中
            self.models.append(model)

        #************* End **************#


    def predict(self, feature):
        '''
        :param feature: 测试集数据，类型为ndarray
        :return: 预测结果，类型为ndarray，如np.array([0, 1, 2, 2, 1, 0])
        '''
        #************* Begin ************#

        # 收集所有模型的预测结果
        predictions = []

        # 让每个模型对测试集进行预测
        for model in self.models:
            pred = model.predict(feature)
            predictions.append(pred)

        # 将预测结果转换为数组，shape为(n_model, n_samples)
        predictions = np.array(predictions)

        # 对每个样本进行投票，选择票数最多的类别
        # 使用Counter统计每个样本的预测结果
        result = []
        for i in range(len(feature)):
            # 获取第i个样本在所有模型中的预测结果
            votes = predictions[:, i]
            # 使用Counter统计，most_common(1)返回票数最多的类别
            most_common_label = Counter(votes).most_common(1)[0][0]
            result.append(most_common_label)

        return np.array(result)

        #************* End **************#
