# https://leetcode.com/problems/design-hashmap/

from typing import List, Optional


class MyHashMap:

    def __init__(self):
        self._values: List[Optional[int]] = [None] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self._values[key] = value

    def get(self, key: int) -> int:
        value = self._values[key]
        if value is None:
            return -1
        return value

    def remove(self, key: int) -> None:
        self._values[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
