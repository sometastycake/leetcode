# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        m = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                value = int(num1[i]) + int(num2[j]) + m
            elif i >= 0:
                value = int(num1[i]) + m
            else:
                value = int(num2[j]) + m
            if value >= 10:
                result.append(str(value - 10))
                m = 1
            else:
                result.append(str(value))
                m = 0
            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1
        if m:
            result.append(str(m))
        result.reverse()
        return ''.join(result)
