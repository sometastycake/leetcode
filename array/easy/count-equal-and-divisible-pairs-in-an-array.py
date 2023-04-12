# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and not (i * j) % k:
                    result += 1
        return result
