# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            mid = (i + j) // 2
            if target < nums[mid]:
                j = mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                return mid
        if nums[mid] < target:
            return mid + 1
        return mid
