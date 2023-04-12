# https://leetcode.com/problems/design-circular-queue/

class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def front(self) -> int:
        if self.head is None:
            return -1
        return self.head.value

    def rear(self) -> int:
        if self.tail is None:
            return -1
        return self.tail.value

    def enqueue(self, value: int):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        self.size -= 1

    def isempty(self) -> bool:
        return self.size == 0


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = Queue()

    def enQueue(self, value: int) -> bool:
        if self.queue.size < self.k:
            self.queue.enqueue(value)
            return True
        return False

    def deQueue(self) -> bool:
        if self.queue.size > 0:
            self.queue.dequeue()
            return True
        return False

    def Front(self) -> int:
        if self.queue.size == 0:
            return -1
        return self.queue.head.value

    def Rear(self) -> int:
        if self.queue.size == 0:
            return -1
        return self.queue.tail.value

    def isEmpty(self) -> bool:
        return self.queue.isempty()

    def isFull(self) -> bool:
        return self.queue.size == self.k
