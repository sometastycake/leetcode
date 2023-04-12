# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import List


class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        n = len(strs)
        result = 0
        for i in range(k):
            j = 0
            while j < n - 1 and strs[j][i] <= strs[j + 1][i]:
                j += 1
            if j < n - 1:
                result += 1
        return result
