# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import defaultdict
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCounter = defaultdict(int)
        for letter in chars:
            charsCounter[letter] += 1
        result = 0
        successWords = set()
        failedWords = set()
        for word in words:
            if word in failedWords:
                continue
            if word in successWords:
                result += len(word)
                continue
            counter = defaultdict(int)
            for letter in word:
                if letter not in charsCounter:
                    failedWords.add(word)
                    break
                counter[letter] += 1
                if counter[letter] > charsCounter[letter]:
                    failedWords.add(word)
                    break
            else:
                result += len(word)
                successWords.add(word)
        return result
