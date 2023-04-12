# https://leetcode.com/problems/rotate-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        length = 0
        nodes = {}
        while node:
            length += 1
            nodes[length] = node
            node = node.next
        k = k - length * (k // length)
        if not k:
            return head
        tmp = []
        for i in range(length - k + 1, length + 1):
            tmp.append(nodes[i].val)
        for i in range(length, k, -1):
            nodes[i].val = nodes[i - k].val
        for i, value in zip(range(1, k + 1), tmp):
            nodes[i].val = value
        return head
