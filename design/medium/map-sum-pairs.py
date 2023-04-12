# https://leetcode.com/problems/map-sum-pairs/


from collections import defaultdict


class Node:

    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def sum(self, prefix: str) -> int:
        result = 0
        node = self.head
        while node:
            if node.key.startswith(prefix):
                result += node.value
            node = node.next
        return result

    def add(self, node: Node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

    def remove(self, node: Node):
        if node is self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        elif node is self.tail:
            n = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            n.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None


class MapSum:

    def __init__(self):
        self.storage = defaultdict(LinkedList)
        self.nodes = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.nodes:
            self.storage[key[0]].remove(self.nodes[key])
        node = Node(key, val)
        self.storage[key[0]].add(node)
        self.nodes[key] = node

    def sum(self, prefix: str) -> int:
        return self.storage[prefix[0]].sum(prefix)
