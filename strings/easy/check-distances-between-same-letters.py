# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        distances = {}
        for i, letter in enumerate(s):
            if letter not in distances:
                distances[letter] = i
            else:
                start = distances[letter]
                distances[letter] = i - start - 1
        for i, d in enumerate(distance):
            letter = chr(ord('a') + i)
            if letter in distances:
                if distances[letter] != d:
                    return False
        return True
