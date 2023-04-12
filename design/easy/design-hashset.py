# https://leetcode.com/problems/design-hashset/

from typing import Optional, List


class MyHashSet:

    def __init__(self):
        self._values: List[Optional[int]] = [None] * 1000001

    def add(self, key: int) -> None:
        self._values[key] = 1

    def remove(self, key: int) -> None:
        self._values[key] = None

    def contains(self, key: int) -> bool:
        return self._values[key] == 1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
