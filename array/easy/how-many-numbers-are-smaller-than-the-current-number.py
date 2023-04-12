# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from collections import defaultdict
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cache = {}
        counter = defaultdict(int)
        for value in nums:
            counter[value] += 1
        result = []
        for i in range(len(nums)):
            if nums[i] in cache:
                result.append(cache[nums[i]])
                continue
            amount = 0
            for j in range(0, nums[i]):
                amount += counter[j]
            result.append(amount)
            cache[nums[i]] = amount
        return result
