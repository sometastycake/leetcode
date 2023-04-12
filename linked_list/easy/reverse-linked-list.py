# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = ListNode(head.val)
        node = head.next
        while node:
            new = ListNode(node.val)
            new.next = current
            current = new
            node = node.next
        return current
