# https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            j = i
            while j < len(s) - 1 and s[j] == s[j + 1]:
                j += 1
            if j == len(s) - 1:
                break
            k = j + 1
            m = j + 1
            while m < len(s) - 1 and s[m] == s[m + 1]:
                m += 1
            l = j - i + 1
            r = m - k + 1
            if l == 1 and r == 1:
                result += 1
            else:
                if l < r:
                    result += l
                else:
                    result += r
            i = k
        return result
