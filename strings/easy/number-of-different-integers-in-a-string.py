# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        result = 0
        integers = set()
        currentNumber = ''
        for letter in word + ' ':
            if not letter.isdigit():
                if currentNumber:
                    number = int(currentNumber)
                    if number not in integers:
                        integers.add(number)
                        result += 1
                    currentNumber = ''
                continue
            currentNumber += letter
        return result
