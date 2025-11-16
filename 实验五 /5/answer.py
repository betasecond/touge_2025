#encoding=utf8
import numpy as np
#adaboost算法
class AdaBoost:
    '''
    input:n_estimators(int):迭代轮数
          learning_rate(float):弱分类器权重缩减系数
    '''
    def __init__(self, n_estimators=50, learning_rate=1.0):
        self.clf_num = n_estimators
        self.learning_rate = learning_rate
    def init_args(self, datasets, labels):
        self.X = datasets
        self.Y = labels
        self.M, self.N = datasets.shape
        # 弱分类器数目和集合
        self.clf_sets = []
        # 初始化weights
        self.weights = [1.0/self.M]*self.M
        # G(x)系数 alpha
        self.alpha = []
    #********* Begin *********#
    def _G(self, features, labels, weights):
        '''
        训练弱分类器（决策树桩）
        input:features(ndarray):数据特征
              labels(ndarray):数据标签
              weights(ndarray):样本权重系数
        return: 最佳分类器参数 (特征索引, 阈值, 分类方向)
        '''
        m = len(features)
        n = len(features[0])

        # 遍历所有特征
        best_clf = {}
        min_error = float('inf')

        for i in range(n):  # 遍历每个特征
            # 获取该特征的所有可能阈值
            feature_values = set([features[j][i] for j in range(m)])

            for v in feature_values:  # 遍历每个可能的阈值
                for direct in ['lt', 'gt']:  # 小于或大于阈值
                    # 计算误差
                    error = 0
                    for j in range(m):
                        # 预测
                        if direct == 'lt':
                            pred = 1 if features[j][i] < v else -1
                        else:
                            pred = 1 if features[j][i] > v else -1

                        # 累加加权误差
                        if pred != labels[j]:
                            error += weights[j]

                    # 更新最佳分类器
                    if error < min_error:
                        min_error = error
                        best_clf = {'dim': i, 'thresh': v, 'direct': direct}

        return best_clf

    # 计算alpha
    def _alpha(self, error):
        '''
        计算弱分类器的权重系数
        '''
        return 0.5 * np.log((1 - error) / max(error, 1e-10))

    # 规范化因子
    def _Z(self, weights, a, clf):
        '''
        计算规范化因子
        '''
        z = 0
        for i in range(self.M):
            # 预测
            pred = self.G(self.X[i], clf['thresh'], clf['direct'])
            pred = 1 if pred == clf['dim'] else -1

            # 根据公式计算
            z += weights[i] * np.exp(-a * self.Y[i] * self.G(self.X[i], clf['thresh'], clf['direct']))

        return z

    # 权值更新
    def _w(self, a, clf, Z):
        '''
        更新样本权重
        '''
        for i in range(self.M):
            # 预测
            pred = self.G(self.X[i], clf['thresh'], clf['direct'])

            # 更新权重
            self.weights[i] = self.weights[i] * np.exp(-a * self.Y[i] * pred) / Z

    # G(x)的线性组合
    def G(self, x, v, direct):
        '''
        单个弱分类器的预测
        '''
        if direct == 'lt':
            return 1 if x < v else -1
        else:
            return 1 if x > v else -1

    def fit(self, X, y):
        '''
        训练AdaBoost模型
        X(ndarray):训练数据
        y(ndarray):训练标签
        '''
        self.init_args(X, y)

        for epoch in range(self.clf_num):
            # 训练弱分类器
            best_clf = self._G(self.X, self.Y, self.weights)

            # 计算误分率
            error = 0
            for i in range(self.M):
                if self.G(self.X[i][best_clf['dim']], best_clf['thresh'], best_clf['direct']) != self.Y[i]:
                    error += self.weights[i]

            # 计算G(x)系数alpha
            a = self._alpha(error)
            self.alpha.append(a)

            # 记录分类器
            self.clf_sets.append(best_clf)

            # 规范化因子
            Z = sum([
                self.weights[i] * np.exp(-a * self.Y[i] *
                self.G(self.X[i][best_clf['dim']], best_clf['thresh'], best_clf['direct']))
                for i in range(self.M)
            ])

            # 权值更新
            for i in range(self.M):
                pred = self.G(self.X[i][best_clf['dim']], best_clf['thresh'], best_clf['direct'])
                self.weights[i] = self.weights[i] * np.exp(-a * self.Y[i] * pred) / Z

    def predict(self, data):
        '''
        预测
        input:data(ndarray):单个样本
        output:预测为正样本返回+1，负样本返回-1
        '''
        result = 0
        for i in range(len(self.clf_sets)):
            clf = self.clf_sets[i]
            pred = self.G(data[clf['dim']], clf['thresh'], clf['direct'])
            result += self.alpha[i] * pred

        return 1 if result > 0 else -1

    #********* End *********#
