# https://leetcode.com/problems/word-pattern/

from collections import Counter, defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        wordsLetters = {}
        wordsCounter = defaultdict(set)
        counter = Counter(pattern)
        for word, letter in zip(words, pattern):
            if letter in wordsLetters and wordsLetters[letter] != word:
                return False
            wordsLetters[letter] = word
            wordsCounter[word].add(letter)
            if len(wordsCounter[word]) > 1:
                return False
            counter[letter] -= 1
        return all(not amount for amount in counter.values())
