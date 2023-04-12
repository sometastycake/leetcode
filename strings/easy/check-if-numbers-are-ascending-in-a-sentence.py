# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        i = 0
        lastNumber = 0
        while i < len(s):
            if s[i].isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number *= 10
                    number += int(s[i])
                    i += 1
                if lastNumber and lastNumber >= number:
                    return False
                lastNumber = number
            else:
                i += 1
        return True
