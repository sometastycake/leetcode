# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:

    def __init__(self):
        self.mapping = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25
        }

    def convert(self, s: str) -> int:
        num = 0
        for digit in s:
            value = self.mapping[digit]
            num *= 10
            num += value
        return num

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstNum = self.convert(firstWord)
        if firstWord == secondWord:
            secondNum = firstNum
        else:
            secondNum = self.convert(secondWord)
        return firstNum + secondNum == self.convert(targetWord)
