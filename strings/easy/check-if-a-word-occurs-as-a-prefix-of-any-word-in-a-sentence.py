# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        currentWord = ''
        wordIndex = 1
        for letter in sentence + ' ':
            if letter != ' ':
                currentWord += letter
                if currentWord == searchWord:
                    return wordIndex
                continue
            currentWord = ''
            wordIndex += 1
        return -1
