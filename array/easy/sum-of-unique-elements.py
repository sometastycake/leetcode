# https://leetcode.com/problems/sum-of-unique-elements/

from collections import defaultdict
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        deleted = set()
        counter = defaultdict(int)
        for num in nums:
            if num not in deleted and not counter[num]:
                result += num
                counter[num] += 1
                deleted.add(num)
            elif counter[num]:
                counter[num] -= 1
                result -= num
        return result
