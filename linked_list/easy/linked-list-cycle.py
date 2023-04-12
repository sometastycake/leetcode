# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nodes = set()
        node = head
        while node:
            h = hash(node)
            if h in nodes:
                return True
            nodes.add(h)
            node = node.next
        return False
