"""
@author:Wang Xinsheng
@File:冒泡排序.py
@description:
@time:2021-03-20 23:47
"""
def bubble_sort(a):
    '''
    从头至尾，交换元素，若前一个比后一个大，则交换，一轮交换过后，最大的一个元素到了最后面，继续下一轮直到所有元素有序。
    :param a:
    :return:
    '''
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(a)


if __name__ == '__main__':
    a = [3,1,5,7,2,4,9,6]
    bubble_sort(a)