任务描述
相关知识
红酒数据分析
编程要求
测试说明
任务描述
本关任务：编写Python代码，实现平均酒精含量的功能。

相关知识
为了完成本关任务，你需要掌握简单的数据分析。

红酒数据分析
sklearn中已经内置的红酒数据，获取红酒数据的代码如下:

from sklearn.datasets import load_wine
wine_dataset = load_wine()
# 打印红酒数据集中的特征的名称
print(wine_dataset['feature_names'])
打印结果如下：

['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
从打印结果可以看出，该数据集中包含了红酒的酒精含量、苹果酸含量、颜色饱和度等信息。

同样我们可以看下红酒的标签名称，代码如下：

from sklearn.datasets import load_wine
wine_dataset = load_wine()
# 打印红酒数据集中的标签的名称
print(wine_dataset['target_names'])
打印结果如下：

['class_0' 'class_1' 'class_2']
可以看出该数据集中红酒的种类总共为3类。也就是说如果用机器学习算法来对其进行分类的话，属于多分类问题。而我们所学习的kNN算法正好可以解决多分类问题。

编程要求
请仔细阅读右侧代码，根据方法内的提示，在Begin - End区域内进行代码补充，完成alcohol_mean函数。该函数需要完成返回红酒数据中的平均酒精含量。其中函数的参数解释如下:

data：红酒数据对象。
测试说明
补充完代码后，点击测评，平台会对你编写的代码进行测试，当你的结果与预期输出一致时，即为通过。

预期输出：平均酒精含量计算正确。

开始你的任务吧，祝你成功！