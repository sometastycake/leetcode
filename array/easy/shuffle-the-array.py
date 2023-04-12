# https://leetcode.com/problems/shuffle-the-array/

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * len(nums)
        k = 0
        for i in range(n):
            result[i + k] = nums[i]
            result[i + k + 1] = nums[i + n]
            k += 1
        return result
