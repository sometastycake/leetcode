# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary = ''
        while node:
            binary += str(node.val)
            node = node.next
        return int(binary, 2)
