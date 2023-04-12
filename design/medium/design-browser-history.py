# https://leetcode.com/problems/design-browser-history/

class Node:

    def __init__(self, url: str):
        self.url = url
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head
        self.current = 1
        self.size = 1
        self.nodes = {self.current: self.head}

    def visit(self, url: str) -> None:
        node = Node(url)
        if self.current < self.size:
            self.nodes[self.current].next = None
            self.tail = self.nodes[self.current]
            self.size = self.current
        self.tail.next = node
        self.tail = self.tail.next
        self.current += 1
        self.size += 1
        self.nodes[self.current] = node

    def back(self, steps: int) -> str:
        if self.current - steps < 1:
            self.current = 1
        else:
            self.current = self.current - steps
        return self.nodes[self.current].url

    def forward(self, steps: int) -> str:
        if self.current + steps > self.size:
            self.current = self.size
        else:
            self.current += steps
        return self.nodes[self.current].url
