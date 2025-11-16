#encoding=utf8
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
def ada_classifier(train_data,train_label,test_data):
    '''
    input:train_data(ndarray):训练数据
          train_label(ndarray):训练标签
          test_data(ndarray):测试标签
    output:predict(ndarray):预测结果
    '''
    #********* Begin *********#

    # 创建AdaBoost分类器
    # 使用默认的决策树作为基学习器
    # n_estimators设置为50个弱学习器
    ada = AdaBoostClassifier(n_estimators=100, learning_rate=1.0, random_state=0)

    # 训练模型
    ada.fit(train_data, train_label)

    # 预测测试数据
    predict = ada.predict(test_data)

    #********* End *********# 
    return predict






























