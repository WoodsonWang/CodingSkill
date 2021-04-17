"""
@author:Wang Xinsheng
@File:21. 合并两个有序链表.py
@description:...
@time:2021-03-31 17:24
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    '''
    暴力破解法
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        index_one = l1
        index_two = l2
        new_list = ListNode(-1)
        pre = new_list
        while index_one and index_two:
            if index_one.val > index_two.val:
                pre.next = index_two
                index_two = index_two.next

            else:
                pre.next = index_one
                index_one = index_one.next

            pre = pre.next

        if index_one == None:
            pre.next = index_two
        else:
            pre.next = index_one

        return new_list.next

    def digui(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.digui(l1.next,l2)
        elif l2.val < l1.val:
            l2.next = self.digui(l2.next,l1)

