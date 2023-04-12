# https://leetcode.com/problems/third-maximum-number/

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        max1 = max2 = max3 = -2 ** 31 - 1
        for value in nums:
            if value > max1:
                max3 = max2
                max2 = max1
                max1 = value
            elif value > max2 and value != max1:
                max3 = max2
                max2 = value
            elif value > max3 and value not in (max1, max2):
                max3 = value
        if max3 == -2 ** 31 - 1:
            return max1
        return max3
