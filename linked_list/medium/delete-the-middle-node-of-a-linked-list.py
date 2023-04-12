# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

from typing import Tuple, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getSize(self, head: ListNode) -> int:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        return size

    def getMiddleNode(self, head: ListNode, size: int) -> Tuple[ListNode, ListNode]:
        middle = size // 2
        index = 0
        node = prev = head
        while index < middle:
            index += 1
            prev = node
            node = node.next
        return prev, node

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        size = self.getSize(head)
        if size == 1:
            return head.next
        premiddle, middle = self.getMiddleNode(head, size)
        premiddle.next = middle.next
        return head
