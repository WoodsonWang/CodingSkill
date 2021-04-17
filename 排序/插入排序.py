"""
@author:Wang Xinsheng
@File:插入排序.py
@description:...
@time:2021-03-21 17:00
"""
from constant import *
def insertion_sort(a):
    for i in range(1,len(a)):
        current = a[i]
        current_index = i
        for j in range(i)[::-1]:
            if current<a[j]:
                a[current_index] = a[j]
                current_index-=1
        a[current_index] = current
    print(a)

if __name__ == '__main__':
    # a = [1]
    insertion_sort(a)
