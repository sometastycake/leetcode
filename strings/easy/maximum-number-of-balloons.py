# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = {'b', 'a', 'l', 'o', 'n'}
        counter = Counter()
        for letter in text:
            if letter in word:
                counter[letter] += 1
        if len(counter) != 5:
            return 0
        counter['o'] //= 2
        counter['l'] //= 2
        return min(counter.values())
