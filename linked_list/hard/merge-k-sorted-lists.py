# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result = None
        for node in lists:
            if not node:
                continue
            pointer = node
            if result is None:
                result = ListNode(pointer.val)
                pointer = pointer.next
            while pointer:
                current = result
                prev = current
                new = ListNode(pointer.val)
                while current and current.val < pointer.val:
                    prev = current
                    current = current.next
                if current is result:
                    new.next = result
                    result = new
                elif current is None:
                    prev.next = new
                else:
                    prev.next = new
                    new.next = current
                pointer = pointer.next
        return result
