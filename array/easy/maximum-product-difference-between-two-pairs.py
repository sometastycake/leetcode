# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        array = list(sorted(nums))
        return (array[-1] * array[-2]) - (array[0] * array[1])
