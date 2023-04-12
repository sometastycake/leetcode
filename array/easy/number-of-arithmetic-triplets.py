# https://leetcode.com/problems/number-of-arithmetic-triplets/

from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                value = nums[j] - nums[i]
                if value > diff:
                    break
                if value != diff:
                    continue
                for k in range(j + 1, len(nums)):
                    value = nums[k] - nums[j]
                    if value > diff:
                        break
                    if value == diff:
                        result += 1
        return result
