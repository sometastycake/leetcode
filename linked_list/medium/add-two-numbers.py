# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def convertListToInt(self, head: ListNode) -> int:
        result = 0
        k = 1
        node = head
        while node:
            result += node.val * k
            node = node.next
            k *= 10
        return result

    def convertIntToList(self, number: int) -> ListNode:
        if number < 10:
            return ListNode(number)
        result = tail = ListNode(number % 10)
        number //= 10
        while number:
            digit = number % 10
            number //= 10
            tail.next = ListNode(digit)
            tail = tail.next
        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        n1 = self.convertListToInt(l1) if l1 else 0
        n2 = self.convertListToInt(l2) if l2 else 0
        return self.convertIntToList(n1 + n2)
