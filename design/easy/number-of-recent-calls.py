# https://leetcode.com/problems/number-of-recent-calls/

class Node:

    def __init__(self, t: int):
        self.t = t
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, t: int) -> None:
        if self.head is None:
            self.head = self.tail = Node(t)
        else:
            self.tail.next = Node(t)
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self) -> None:
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

    def clear(self, initialPeriod: int) -> None:
        if self.head is None:
            return
        while self.head and self.head.t < initialPeriod:
            self.dequeue()


class RecentCounter:

    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.clear(t - 3000)
        self.queue.enqueue(t)
        return self.queue.size
