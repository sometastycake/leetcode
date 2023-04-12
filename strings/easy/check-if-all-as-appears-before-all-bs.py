# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        lastB = -1
        lastA = -1
        for i, letter in enumerate(s):
            if letter == 'a':
                lastA = i
                if lastB != -1 and lastA > lastB:
                    return False
            elif letter == 'b':
                lastB = i
                if lastA != -1 and lastB < lastA:
                    return False
        return True
