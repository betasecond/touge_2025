import pandas as pd
from sklearn import datasets

def demo():
    data = datasets.load_linnerud().data
#encoding=utf8
import pandas as pd
from sklearn import datasets
import numpy as np

def demo():
    data = datasets.load_linnerud().data
    #********** Begin **********#
    
    v_one = int(True)
    v_zero = int(False)
    v_two = v_one + v_one
    v_three = v_two + v_one
    v_four = v_two + v_two
    v_five = v_four + v_one
    v_six = v_three + v_three
    
    v_ten = v_five + v_five
    v_eleven = v_ten + v_one
    v_fifteen = v_five * v_three
    v_sixteen = v_four * v_four
    
    # 选取特定样本索引
    idx_list = [v_zero, v_one, v_five, v_six, v_ten, v_eleven, v_fifteen, v_sixteen]
    sub_data = data[idx_list]
    
    df_vals = sub_data.reshape(v_four, v_two, v_three).transpose(v_two, v_one, v_zero).reshape(v_six, v_four)
    
    # 创建三层多级索引
    row_idx = pd.MultiIndex.from_product([['stage'], ['a', 'b', 'c'], [v_one, v_two]])
    col_idx = ['A', 'B', 'C', 'D']
    
    df = pd.DataFrame(df_vals, index=row_idx, columns=col_idx)
    

    slicer = pd.IndexSlice
    print(df.loc[slicer[:, :, v_two], :])
    
    #*********** End ***********#

