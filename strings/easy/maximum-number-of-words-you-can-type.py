# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        broken = False
        brokenLetters = set(brokenLetters)
        for letter in text + ' ':
            if letter != ' ':
                if letter in brokenLetters:
                    broken = True
                continue
            if not broken:
                result += 1
            broken = False
        return result
