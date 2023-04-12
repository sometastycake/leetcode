# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(ord('z'), ord('a') - 1, -1):
            letter = chr(i)
            if letter.lower() in s and letter.upper() in s:
                return letter.upper()
        return ''
