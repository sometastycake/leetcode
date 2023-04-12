# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        val = self.stack.pop()
        return val

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            size = len(self.stack)
        else:
            size = k
        for i in range(0, size):
            self.stack[i] += val
