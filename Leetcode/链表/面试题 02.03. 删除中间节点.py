"""
@author:Wang Xinsheng
@File:面试题 02.03. 删除中间节点.py
@description:...
@time:2021-03-31 16:25
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next