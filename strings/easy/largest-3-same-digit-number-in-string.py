# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        segment = ''
        for digit in num:
            if not segment or segment[-1] == digit:
                segment += digit
            else:
                if len(segment) >= 3:
                    segment = segment[:3]
                    if not result or int(segment) > int(result):
                        result = segment
                segment = digit
        if len(segment) >= 3:
            segment = segment[:3]
            if not result or int(segment) > int(result):
                result = segment
        return result
