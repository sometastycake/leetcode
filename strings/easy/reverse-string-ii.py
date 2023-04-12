# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        array = list(s)
        i = 0
        while i < len(s):
            j = i
            m = j + k - 1
            if m > len(s) - 1:
                m = len(s) - 1
            while j < m:
                tmp = array[j]
                array[j] = array[m]
                array[m] = tmp
                j += 1
                m -= 1
            i += 2 * k
        return ''.join(array)
