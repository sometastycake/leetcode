# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
        n = str(n)
        s = []
        for i in range(len(n) - 1, -1, -3):
            if i - 2 >= 0:
                s.append(n[i - 2: i + 1])
            else:
                s.append(n[:i + 1])
        s.reverse()
        return '.'.join(s)
