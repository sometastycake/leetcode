# https://leetcode.com/problems/keyboard-row/

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = {'t', 'q', 'w', 'r', 'e', 'y', 'p', 'u', 'i', 'o'}
        secondRow = {'f', 'h', 'k', 'j', 's', 'l', 'g', 'd', 'a'}
        thirdRow = {'x', 'z', 'v', 'n', 'm', 'c', 'b'}
        result = []
        for word in words:
            counter = {'1': 0, '2': 0, '3': 0}
            success = True
            for letter in word:
                letter = letter.lower()
                if letter in firstRow:
                    counter['1'] += 1
                    if counter['2'] > 0 or counter['3'] > 0:
                        success = False
                elif letter in secondRow:
                    counter['2'] += 1
                    if counter['1'] > 0 or counter['3'] > 0:
                        success = False
                else:
                    counter['3'] += 1
                    if counter['1'] > 0 or counter['2'] > 0:
                        success = False
                if not success:
                    break
            if success:
                result.append(word)
        return result
