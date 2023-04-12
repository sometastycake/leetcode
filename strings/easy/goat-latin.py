# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        currentWord = []
        wordIndex = 1
        ma = ['m', 'a']
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        customSentence = sentence + ' '
        for letter in customSentence:
            if letter != ' ':
                currentWord.append(letter)
                continue
            if currentWord[0] in vowels:
                currentWord += ma
            else:
                currentWord += [currentWord[0]] + ma
                currentWord[0] = ''
            currentWord += ['a'] * wordIndex
            result.append(''.join(currentWord))
            currentWord = []
            wordIndex += 1
        return ' '.join(result)
