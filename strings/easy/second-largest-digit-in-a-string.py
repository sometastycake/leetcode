# https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        firstLargest = -1
        secondLargest = -1
        for letter in s:
            if not letter.isdigit():
                continue
            digit = int(letter)
            if digit > firstLargest:
                secondLargest = firstLargest
                firstLargest = digit
            elif digit > secondLargest and digit != firstLargest:
                secondLargest = digit
        return secondLargest
