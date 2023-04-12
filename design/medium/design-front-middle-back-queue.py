# https://leetcode.com/problems/design-front-middle-back-queue/


class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushFront(self, val: int):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def pushBack(self, val: int):
        if self.head is None:
            self.head = self.tail = Node(val)
        else:
            node = Node(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def popFront(self) -> int:
        if self.head is None:
            return -1
        val = self.head.val
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        self.size -= 1
        return val

    def popBack(self) -> int:
        if self.tail is None:
            return -1
        val = self.tail.val
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        node.prev = None
        self.size -= 1
        return val

    def getMiddle(self) -> Node:
        i = 1
        middle = self.size // 2
        node = self.head
        while i < middle:
            i += 1
            node = node.next
        return node

    def pushMiddle(self, val: int):
        if self.head is None:
            self.head = self.tail = Node(val)
            self.size += 1
        else:
            middle = self.getMiddle()
            if middle.next is None:
                self.pushFront(val)
            else:
                node = Node(val)
                node.next = middle.next
                node.prev = middle
                middle.next.prev = node
                middle.next = node
                self.size += 1

    def popMiddle(self) -> int:
        if self.head is None:
            return -1
        if self.size in (1, 2):
            return self.popFront()
        middle = self.getMiddle()
        if self.size % 2:
            middle = middle.next
        val = middle.val
        middle.prev.next = middle.next
        middle.next.prev = middle.prev
        middle.next = middle.prev = None
        self.size -= 1
        return val


class FrontMiddleBackQueue:

    def __init__(self):
        self.list = LinkedList()

    def pushFront(self, val: int) -> None:
        self.list.pushFront(val)

    def pushMiddle(self, val: int) -> None:
        self.list.pushMiddle(val)

    def pushBack(self, val: int) -> None:
        self.list.pushBack(val)

    def popFront(self) -> int:
        return self.list.popFront()

    def popMiddle(self) -> int:
        return self.list.popMiddle()

    def popBack(self) -> int:
        return self.list.popBack()
