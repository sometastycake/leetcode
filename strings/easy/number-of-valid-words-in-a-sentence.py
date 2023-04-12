# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        word = ''
        isDigit = False
        hyphens = []
        punctuationsMarks = []
        result = 0
        for index, letter in enumerate(sentence + ' '):
            if letter != ' ':
                if not word:
                    beginWordIndex = index
                    isDigit, hyphens, punctuationsMarks = False, [], []
                word += letter
                if letter.isdigit():
                    isDigit = True
                elif letter == '-':
                    hyphens.append(index - beginWordIndex)  # noqa
                elif letter in ('!', '.', ','):
                    punctuationsMarks.append(letter)
                continue
            if not word:
                continue
            if isDigit or len(hyphens) > 1 or len(punctuationsMarks) > 1:
                word = ''
                continue
            if hyphens:
                if len(word) < 3 or '-' in (word[0], word[-1]):
                    word = ''
                    continue
                i = hyphens[0]
                if not word[i - 1].isalpha() or not word[i + 1].isalpha():
                    word = ''
                    continue
            if punctuationsMarks:
                mark = punctuationsMarks[0]
                if word[-1] != mark:
                    word = ''
                    continue
            result += 1
            word, isDigit, hyphens, punctuationsMarks = '', False, [], []
        return result
