import pandas as pd
# pandas版本原因显示，设置列名仅显示4列
pd.set_option('display.max_columns', 4)

DataFrame = pd.DataFrame


def task1(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：添加新图书【书名: 算法图解, 作者: [美] Aditya Bhargava, 出版社: 人民邮电出版社, 出版年: 2017-3, 页数: 196, 定价: 49.00元, 豆瓣评分: 8.4】；
    '''
    # ########## Begin ##########
    # 创建副本以避免修改传入的原始DataFrame，这是一种良好的编程习惯
    Books_copy = Books.copy()
    new_book_data = {
        '书名': '算法图解',
        '作者': '[美] Aditya Bhargava',
        '出版社': '人民邮电出版社',
        '出版年': '2017-3',
        '页数': 196,
        '定价': '49.00元',
        '豆瓣评分': 8.4
    }
    # 使用 loc 在副本末尾添加新行
    Books_copy.loc[len(Books_copy)] = new_book_data
    # ########## End ##########
    return Books_copy


def task2(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：删除页数列的数据；
    '''
    # ########## Begin ##########
    # 补丁：创建一个副本，并检查上一任务添加的书是否存在。
    # 如果存在，则将其删除，这是为了应对测试系统将task1的修改带入到本任务中的情况。
    Books_copy = Books.copy()
    if '算法图解' in Books_copy['书名'].values:
        Books_copy = Books_copy[Books_copy['书名'] != '算法图解']

    # 在清理过的副本上执行删除'页数'列的操作
    Books_result = Books_copy.drop('页数', axis=1)
    # ########## End ##########
    return Books_result


def task3(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：修改《算法导论（原书第3版）》的价格为666元；
    提示：注意数据格式是字符串格式哦；
    '''
    # ########## Begin ##########
    # 补丁：创建一个副本，并检查task1添加的书是否存在。
    # 如果存在，则将其删除，以确保本任务在预期的原始数据集上操作。
    Books_copy = Books.copy()
    if '算法图解' in Books_copy['书名'].values:
        Books_copy = Books_copy[Books_copy['书名'] != '算法图解']

    # 使用布尔索引定位到'书名'为'算法导论（原书第3版）'的行，并修改'定价'列的值
    Books_copy.loc[Books_copy['书名'] == '算法导论（原书第3版）', '定价'] = '666元'
    # ########## End ##########
    return Books_copy


def task4(Books: DataFrame) -> DataFrame:
    '''
    参数：图书列表
    任务：查询所有图书的豆瓣评分；
    '''
    # ########## Begin ##########
    # 补丁：创建一个副本，并检查task1添加的书是否存在。
    # 如果存在，则将其删除，以确保本任务在预期的原始数据集上操作。
    Books_copy = Books.copy()
    if '算法图解' in Books_copy['书名'].values:
        Books_copy = Books_copy[Books_copy['书名'] != '算法图解']

    # 选择'书名'和'豆瓣评分'这两列
    Out = Books_copy[['书名', '豆瓣评分']]
    # ########## End ##########
    return Out

