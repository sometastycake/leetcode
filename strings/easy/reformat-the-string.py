# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        digits = []
        letters = []
        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                letters.append(i)
        if abs(len(digits) - len(letters)) > 1:
            return ''
        result = ''
        i, j = 0, 0
        if len(digits) > len(letters):
            s1, s2 = digits, letters
        else:
            s1, s2 = letters, digits
        while i < len(s1) or j < len(s2):
            if i < len(s1) and j < len(s2):
                result += s1[i]
                result += s2[j]
                i += 1
                j += 1
            elif i < len(s1):
                result += s1[i]
                i += 1
            else:
                result += s2[j]
                j += 1
        return result
