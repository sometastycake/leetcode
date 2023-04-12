# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = '1'
        for digit in n:
            if digit > maxDigit:
                maxDigit = digit
                if maxDigit == '9':
                    return 9
        return int(maxDigit)
