# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for value in candies:
            result.append(value + extraCandies >= maxCandies)
        return result
