# https://leetcode.com/problems/count-pairs-of-similar-strings/

from collections import defaultdict


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = defaultdict(set)
        result = 0
        for i in range(len(words)):
            if i not in counter:
                counter[i] = set(words[i])
            for j in range(i + 1, len(words)):
                if j not in counter:
                    counter[j] = set(words[j])
                if counter[i] == counter[j]:
                    result += 1
        return result
