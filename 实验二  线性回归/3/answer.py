#encoding=utf8
import numpy as np

#mse
def mse_score(y_predict,y_test):
    mse = np.mean((y_predict-y_test)**2)
    return mse

#r2
def r2_score(y_predict,y_test):
    '''
    input:y_predict(ndarray):预测值
          y_test(ndarray):真实值
    output:r2(float):r2值
    '''
    #********* Begin *********#
    # 为确保形状一致，先展平
    y_predict_flat = y_predict.flatten()
    y_test_flat = y_test.flatten()

    # 1. 计算分子：预测值与真实值之间的残差平方和 (SSR)
    numerator = np.sum(np.square(y_predict_flat - y_test_flat))

    # 2. 计算真实值的均值
    y_mean = np.mean(y_test_flat)

    # 3. 计算分母：真实值与其均值之间的差值平方和 (SST)
    denominator = np.sum(np.square(y_test_flat - y_mean))

    # 4. 计算 R-Squared
    # (增加一个极小值防止分母为0)
    epsilon = 1e-8
    r2 = 1 - (numerator / (denominator + epsilon))

    #********* End *********#
    return r2

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
        ones_col = np.ones((train_data.shape[0], 1))
        X_b = np.hstack((ones_col, train_data))

        # 2. 应用正规方程: theta = (X_b.T * X_b)^-1 * X_b.T * Y
        # (为了数值稳定性，实际应用中会用np.linalg.solve，但按题目要求用inv)
        term1 = np.dot(X_b.T, X_b)
        term2 = np.linalg.inv(term1)
        term3 = np.dot(X_b.T, train_label)

        self.theta = np.dot(term2, term3)
        #********* End *********#
        return self

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