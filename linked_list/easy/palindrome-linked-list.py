# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        node = head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        node = head
        for i in range(len(values) - 1, len(values) // 2 - 1, -1):
            if node.val != values[i]:
                return False
            node = node.next
        return True
