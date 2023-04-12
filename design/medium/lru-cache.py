# https://leetcode.com/problems/lru-cache/

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
        self.size = 0

    def addHead(self, node: Node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = self.head.prev
        self.size += 1

    def removeTail(self):
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        node.prev = None
        self.size -= 1

    def removeHead(self):
        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        self.size -= 1

    def remove(self, node: Node):
        if node is self.head:
            self.removeHead()
        elif node is self.tail:
            self.removeTail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
            self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.cachelist = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        if node is not self.cachelist.head:
            self.cachelist.remove(node)
            self.cachelist.addHead(node)
        return self.nodes[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            if self.cachelist.size == self.capacity:
                lrukey = self.cachelist.tail.key
                del self.nodes[lrukey]
                self.cachelist.removeTail()
            node = Node(key, value)
            self.nodes[key] = node
            self.cachelist.addHead(node)
        else:
            node = self.nodes[key]
            if node is not self.cachelist.head:
                self.cachelist.remove(node)
                self.cachelist.addHead(node)
            self.nodes[key].value = value
