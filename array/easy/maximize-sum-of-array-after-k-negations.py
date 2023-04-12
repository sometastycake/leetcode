# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = list(sorted(nums))
        i = 0
        while i < len(nums) and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            if not k:
                return sum(nums)
            i += 1
        if i < len(nums) and nums[i] == 0:
            return sum(nums)
        if not k % 2:
            return sum(nums)
        minIndex = 0
        for j in range(1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[minIndex] = -nums[minIndex]
        return sum(nums)
