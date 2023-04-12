# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        newHead = newTail = ListNode()
        node = head.next
        currentSum = 0
        while node:
            while node and node.val:
                currentSum += node.val
                node = node.next
            newTail.next = ListNode(currentSum)
            newTail = newTail.next
            currentSum = 0
            node = node.next
        return newHead.next
