# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        t = ''
        for letter in s:
            t += str(ord(letter) - ord('a') + 1)
        t = int(t)
        sm = 0
        for _ in range(k):
            sm = 0
            while t:
                digit = t % 10
                sm += digit
                t //= 10
            t = sm
        return sm
