# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        word = ''
        for letter in title + ' ':
            if letter == ' ':
                if len(word) in (1, 2):
                    result.append(word.lower())
                else:
                    result.append(word.capitalize())
                word = ''
                continue
            word += letter
        return ' '.join(result)
    