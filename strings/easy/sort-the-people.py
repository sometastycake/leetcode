# https://leetcode.com/problems/sort-the-people/

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        array = []
        for name, height in zip(names, heights):
            array.append((name, height))
        sortedarray = sorted(array, key=lambda item: item[1], reverse=True)
        return [name for name, height in sortedarray]
