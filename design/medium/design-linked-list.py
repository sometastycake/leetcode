# https://leetcode.com/problems/design-linked-list/

from typing import Optional


class Node:

    def __init__(self, value: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.value = value
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getNodeByIndex(self, index: int) -> Node:
        i = 0
        node = self.head
        while node:
            if i == index:
                return node
            node = node.next
            i += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self.getNodeByIndex(index).value

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        new = Node(val)
        node = self.getNodeByIndex(index)
        new.prev = node.prev
        new.next = node
        node.prev = new
        new.prev.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.getNodeByIndex(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
        self.size -= 1
