# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:

    def search(self, nums: List[int], target: int, start: int, end: int) -> int:
        i = start
        j = end
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = self.search(nums, target, 0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        result = [index, index]
        i = result[0]
        while i != -1 and i > 0:
            i = self.search(nums, target, 0, i - 1)
            if i != -1 and i < result[0]:
                result[0] = i
        i = result[1]
        while i != -1 and i < len(nums) - 1:
            i = self.search(nums, target, i + 1, len(nums) - 1)
            if i != -1 and i > result[1]:
                result[1] = i
        return result
