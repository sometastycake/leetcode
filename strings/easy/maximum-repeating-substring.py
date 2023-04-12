# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result = 0
        i = 0
        while i < len(sequence):
            sequenceCount = 0
            j = i
            while j < len(sequence) and sequence[j: j + len(word)] == word:
                sequenceCount += 1
                j += len(word)
            if sequenceCount > result:
                result = sequenceCount
            i += 1
        return result
