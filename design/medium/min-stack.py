# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None:
            self.min = val
        elif val < self.min:
            self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
