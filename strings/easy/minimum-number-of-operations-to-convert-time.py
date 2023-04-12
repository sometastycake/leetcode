# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currentHours = int(current[:current.index(':')])
        currentMinutes = int(current[current.index(':') + 1:])
        correctHours = int(correct[:correct.index(':')])
        correctMinutes = int(correct[correct.index(':') + 1:])
        minutes = [60, 15, 5, 1]
        difference = (correctHours - currentHours) * 60 + (correctMinutes - currentMinutes)
        result = 0
        for minute in minutes:
            if minute <= difference:
                amount = difference // minute
                result += amount
                difference -= amount * minute
        return result
