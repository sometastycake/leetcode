# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        currentGroup = [''] * k
        j = 0
        for letter in reversed(s):
            if letter == '-':
                continue
            currentGroup[k - j - 1] = letter.upper()
            j += 1
            if j == k:
                result.append(''.join(currentGroup))
                j = 0
        if j:
            result.append(''.join(currentGroup[k - j:]))
        return '-'.join(result[::-1])
