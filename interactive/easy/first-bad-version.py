# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n: int) -> int:
        i = 1
        j = n
        while i <= j:
            mid = (i + j) // 2
            isBad = isBadVersion(mid)  # noqa
            if not isBad:
                i = mid + 1
            else:
                j = mid - 1
        return i
