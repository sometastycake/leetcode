# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            numbers = []
            for i in range(0, len(s), k):
                numbers.append(s[i: i + k])
            sm = ''
            for number in numbers:
                value = 0
                for digit in number:
                    value += int(digit)
                sm += str(value)
            s = str(sm)
        return s
