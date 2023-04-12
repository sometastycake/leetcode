# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            freq = nums[i]
            val = nums[i + 1]
            result += [val] * freq
            i += 2
        return result
