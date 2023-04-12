# https://leetcode.com/problems/lfu-cache/

from collections import defaultdict


class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    @property
    def empty(self) -> bool:
        return self.head is None

    def remove(self, node: Node) -> None:
        if node is self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            if not self.tail:
                self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = node.prev = None

    def insertAtHead(self, node: Node) -> None:
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        node.prev = None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counterList = defaultdict(LinkedList)
        self.counter = {}
        self.cache = {}
        self.min = 1

    def increment(self, key: int) -> None:
        previousCounter = self.counter[key]
        node = self.cache[key]
        self.counterList[previousCounter].remove(node)
        self.counterList[previousCounter + 1].insertAtHead(node)
        self.counter[key] += 1
        while self.counterList[self.min].empty:
            self.min += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.increment(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity == len(self.cache):
                # LRU value which have minimum frequency of using
                node = self.counterList[self.min].tail
                # Remove node
                self.counterList[self.min].remove(node)
                del self.cache[node.key]
                del self.counter[node.key]
                while self.counterList[self.min].empty and self.min > 0:
                    self.min -= 1
            node = Node(key, value)
            self.counter[key] = 1
            self.cache[key] = node
            self.counterList[1].insertAtHead(node)
            self.min = 1
        else:
            oldvalue = self.cache[key].value
            if value != oldvalue:
                self.cache[key].value = value
            self.increment(key)
