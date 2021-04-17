"""
@author:Wang Xinsheng
@File:面试题 02.02. 返回倒数第 k 个节点.py
@description:...
@time:2021-03-31 15:55
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        start_one = head
        start_two = head
        for i in range(k-1):
            start_two = start_two.next
        while start_two.next!=None:
            start_two = start_two.next
            start_one = start_one.next
        print(start_one.val)
