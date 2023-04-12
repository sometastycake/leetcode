# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head = None
        cur = None
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            if not head:
                head = node
                cur = head
            else:
                cur.next = node
                cur = cur.next
        if list1 and not list2:
            remainingList = list1
        elif not list1 and list2:
            remainingList = list2
        else:
            remainingList = None
        if remainingList:
            while remainingList:
                node = ListNode(remainingList.val)
                if not head:
                    head = node
                    cur = head
                else:
                    cur.next = node
                    cur = cur.next
                remainingList = remainingList.next
        return head
