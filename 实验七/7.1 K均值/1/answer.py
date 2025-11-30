#encoding=utf8    
import numpy as np

def distance(x,y,p=2):
    '''
    input:x(ndarray):第一个样本的坐标
          y(ndarray):第二个样本的坐标
          p(int):等于1时为曼哈顿距离，等于2时为欧氏距离
    output:distance(float):x到y的距离      
    ''' 
    #********* Begin *********#
    diff = np.abs(x - y)
    dis = np.power(np.sum(np.power(diff, p)), 1/p)
    return dis
    #********* End *********#