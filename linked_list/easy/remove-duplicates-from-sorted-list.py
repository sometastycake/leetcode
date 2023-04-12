# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = head
        node = head.next
        while node:
            if prev.val == node.val:
                prev.next = node.next
                node = prev.next
                continue
            prev = node
            node = node.next
        return head
