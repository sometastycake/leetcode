# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0
        noPairs = set()
        pairs = {}
        nums = list(sorted(nums))
        for i in range(len(nums) - 1):
            if nums[i] in noPairs:
                continue
            if nums[i] in pairs:
                result += pairs[nums[i]]
                continue
            amount = 0
            for j in range(i + 1, len(nums)):
                diff = abs(nums[i] - nums[j])
                if diff > k:
                    break
                if diff == k:
                    amount += 1
            if amount:
                result += amount
                pairs[nums[i]] = amount
            else:
                noPairs.add(nums[i])
        return result
