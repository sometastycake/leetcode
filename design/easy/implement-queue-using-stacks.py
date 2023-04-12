# https://leetcode.com/problems/implement-queue-using-stacks/

class Node:

    def __init__(self, x: int):
        self.x = x
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    @property
    def empty(self) -> bool:
        return self.size == 0

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = self.tail = Node(x)
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.size += 1

    def pop(self) -> int:
        x = self.head.x
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return x

    def peek(self) -> int:
        return self.head.x


class MyQueue:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty
