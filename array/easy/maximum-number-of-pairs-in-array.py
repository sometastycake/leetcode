# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = {}
        result = [0, len(nums)]
        for i in range(len(nums)):
            if nums[i] not in pairs:
                pairs[nums[i]] = i
            else:
                result[0] += 1
                result[1] -= 2
                del pairs[nums[i]]
        return result
