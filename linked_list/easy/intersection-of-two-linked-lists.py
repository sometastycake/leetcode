# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashA = {}
        node = headA
        while node:
            hashA[hash(node)] = node
            node = node.next
        node = headB
        while node:
            value = hash(node)
            if value in hashA:
                return hashA[value]
            node = node.next
        return None
