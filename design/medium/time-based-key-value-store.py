# https://leetcode.com/problems/time-based-key-value-store/

from collections import defaultdict
from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.storage: Dict[str, List[Tuple[str, int]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def search(self, key: str, timestamp: int) -> int:
        values = self.storage[key]
        i = 0
        j = len(values) - 1
        while i <= j:
            mid = (i + j) // 2
            if values[mid][1] == timestamp:
                return mid
            if timestamp < values[mid][1]:
                j = mid - 1
            else:
                i = mid + 1
        return i - 1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage or timestamp < self.storage[key][0][1]:
            return ''
        values = self.storage[key]
        if timestamp > values[-1][1]:
            return values[-1][0]
        index = self.search(key, timestamp)
        return values[index][0]
