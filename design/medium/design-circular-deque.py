# https://leetcode.com/problems/design-circular-deque/

class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertFront(self, value: int):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertLast(self, value: int):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def deleteFront(self):
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        self.size -= 1

    def deleteLast(self):
        if self.tail is None:
            return
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        node.prev = None
        self.size -= 1


class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.list = LinkedList()

    def insertFront(self, value: int) -> bool:
        if self.list.size < self.k:
            self.list.insertFront(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.list.size < self.k:
            self.list.insertLast(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.list.size > 0:
            self.list.deleteFront()
            return True
        return False

    def deleteLast(self) -> bool:
        if self.list.size > 0:
            self.list.deleteLast()
            return True
        return False

    def getFront(self) -> int:
        if self.list.size == 0:
            return -1
        return self.list.head.value

    def getRear(self) -> int:
        if self.list.size == 0:
            return -1
        return self.list.tail.value

    def isEmpty(self) -> bool:
        return self.list.size == 0

    def isFull(self) -> bool:
        return self.list.size == self.k
