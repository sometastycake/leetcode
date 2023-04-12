# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from collections import Counter, defaultdict


class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        if all(freq == 1 for freq in counter.values()) or len(counter) == 1:
            return True
        values = list(counter.values())
        if all(value == values[0] for value in values):
            return False
        frequency = defaultdict(int)
        for letter, amount in counter.items():
            frequency[amount] += 1
        if len(frequency) == 1:
            return True
        if len(frequency) == 2:
            maxF = max(frequency.keys())
            minF = min(frequency.keys())
            return (minF == 1 and frequency[minF] == 1) or (abs(minF - maxF) == 1 and frequency[maxF] == 1)
        return False
