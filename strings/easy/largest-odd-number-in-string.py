# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            digit = num[i]
            if int(digit) % 2:
                return num[: i + 1]
        return ''
