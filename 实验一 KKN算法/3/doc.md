任务描述
相关知识
在sklearn中使用KNeighborsRegressor
编程要求
测试说明
任务描述
本关任务：编写一个能对数据进行回归的程序。

相关知识
为了完成本关任务，你需要掌握在sklearn中使用KNeighborsRegressor。

在sklearn中使用KNeighborsRegressor
在使用kNN算法进行分类器时，我们是这样子使用sklearn库的：

from sklearn.neighbors import KNeighborsClassifier
clf=KNeighborsClassifier() #生成K近邻分类器
clf.fit(train_feature, train_label)               #训练分类器
predict_result=clf.predict(test_feature)           #进行预测
而对应的，当我们需要使用kNN算法进行回归器时，只需要把KNeighborsClassifier换成KNeighborsRegressor即可。代码如下:

from sklearn.neighbors import KNeighborsRegressor
clf=KNeighborsRegressor() #生成K近邻分类器
clf.fit(train_feature, train_label)               #训练分类器
predict_result=clf.predict(test_feature)           #进行预测
KNeighborsRegressor和KNeighborsClassifier的参数是完全一样的，所以在优化模型时可以参考上一关的内容。

编程要求
请仔细阅读右侧代码，根据方法内的提示，在Begin - End区域内进行代码补充，具体任务如下：

完成regression函数。函数需要完成的功能是使用KNeighborsRegressor对test_feature进行分类。其中函数的参数如下：

train_feature: 训练集数据；

train_label: 训练集标签；

test_feature: 测试集数据。

测试说明
平台会对你返回的预测结果来计算准确率，你只需完成regression函数即可。r2 score高于0.75视为过关。

预期输出：你的r2 score高于0.75。

开始你的任务吧，祝你成功！