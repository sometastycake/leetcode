# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = {}
        node = head
        i = 0
        while node:
            i += 1
            nodes[i] = node
            node = node.next
        return nodes[i // 2 + 1]
