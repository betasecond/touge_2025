#encoding=utf8
import numpy as np

def mse_score(y_predict,y_test):
    '''
    input:y_predict(ndarray):预测值
          y_test(ndarray):真实值
    ouput:mse(float):mse损失函数值
    '''
    #********* Begin *********#
    # 为确保形状一致，先将输入展平
    y_predict_flat = y_predict.flatten()
    y_test_flat = y_test.flatten()

    # 计算 (真实值 - 预测值) 的平方
    squared_errors = np.square(y_test_flat - y_predict_flat)

    # 计算均方误差
    mse = np.mean(squared_errors)
    #********* End *********#
    return mse

class LinearRegression :
    def __init__(self):
        '''初始化线性回归模型'''
        self.theta = None

    def fit_normal(self,train_data,train_label):
        '''
        input:train_data(ndarray):训练样本
               train_label(ndarray):训练标签
        '''
        #********* Begin *********#
        # 1. 为 train_data 添加偏置项 x0 = 1
        # 创建一个 (m, 1) 的全 1 矩阵，m 为样本数
        ones_col = np.ones((train_data.shape[0], 1))
        # 使用 hstack 将 ones_col 和 train_data 水平拼接
        X_b = np.hstack((ones_col, train_data))

        # 2. 应用正规方程: theta = (X_b.T * X_b)^-1 * X_b.T * Y

        # 计算 X_b.T * X_b
        term1 = np.dot(X_b.T, X_b)

        # 计算 (X_b.T * X_b)^-1
        term2 = np.linalg.inv(term1)

        # 计算 X_b.T * Y
        term3 = np.dot(X_b.T, train_label)

        # 计算 theta
        self.theta = np.dot(term2, term3)
        #********* End *********#
        return self.theta

    def predict(self,test_data):
        '''
        input:test_data(ndarray):测试样本
        '''
        #********* Begin *********#
        # 1. 同样为 test_data 添加偏置项 x0 = 1
        ones_col = np.ones((test_data.shape[0], 1))
        X_test_b = np.hstack((ones_col, test_data))

        # 2. 计算预测值: Y_pred = X_test_b * theta
        y_predict = np.dot(X_test_b, self.theta)

        return y_predict
        #********* End *********#