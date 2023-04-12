# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List


class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        orderIndexes = {}
        for i, letter in enumerate(order):
            orderIndexes[letter] = i
        for i in range(len(words) - 1):
            wordFirst = words[i]
            wordSecond = words[i + 1]
            n = len(wordFirst)
            m = len(wordSecond)
            j, k = 0, 0
            while j < n and k < m and orderIndexes[wordFirst[j]] == orderIndexes[wordSecond[k]]:
                j += 1
                k += 1
            if j < n and k < m:
                if orderIndexes[wordFirst[j]] > orderIndexes[wordSecond[k]]:
                    return False
            elif n > m:
                return False
        return True
