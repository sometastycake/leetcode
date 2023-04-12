# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        counter = defaultdict(int)
        for i in range(len(num)):
            counter[int(num[i])] += 1
        for i in range(len(num)):
            if counter[i] != int(num[i]):
                return False
        return True
