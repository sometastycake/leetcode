# https://leetcode.com/problems/design-an-ordered-stream/

from typing import List, Optional


class OrderedStream:

    def __init__(self, n: int):
        self.array: List[Optional[str]] = [None] * (n + 1)
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey - 1] = value
        result = []
        while self.pointer < len(self.array) and self.array[self.pointer] is not None:
            result.append(self.array[self.pointer])
            self.pointer += 1
        return result
