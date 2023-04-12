# https://leetcode.com/problems/min-max-game/

from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while len(nums) > 1:
            fn = min
            result = []
            for i in range(0, len(nums), 2):
                result.append(fn(nums[i], nums[i + 1]))
                fn = max if fn is min else min
            nums = result
        return nums[0]
