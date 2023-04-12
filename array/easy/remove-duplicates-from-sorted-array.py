# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i < len(nums) - k:
            j = i + 1
            while j < len(nums) - k and nums[j] == nums[i]:
                j += 1
            if j > i + 1:
                tmp = j
                t = 0
                for index in range(j, len(nums) - k):
                    nums[i + t + 1] = nums[index]
                    t += 1
                k += tmp - (i + 1)
            i += 1
        return len(nums) - k
