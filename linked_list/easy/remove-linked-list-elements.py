# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        node = prev = head
        while node:
            if node.val != val:
                prev = node
                node = node.next
                continue
            if node is head:
                head = head.next
                node = prev = head
                continue
            prev.next = node.next
            node = prev
        return head
