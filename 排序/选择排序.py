"""
@author:Wang Xinsheng
@File:选择排序.py
@description:...
@time:2021-03-21 0:18
"""
from constant import *
'''
列表操作，[a:b:c]
从a开始到b 步长为c
'''

def selection_sort(a):
    '''
    数组最后为有序区
    :param a:
    :return:
    '''
    for i in range(len(a))[::-1]:
        # 倒序
        max_index = i
        for j in range(i):
            if a[max_index] < a[j]:
                max_index = j
        temp = a[i]
        a[i] = a[max_index]
        a[max_index] = temp

    print(a)


if __name__ == '__main__':
    selection_sort(a)
