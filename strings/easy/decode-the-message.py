# https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        newkey = ''
        newkeySearch = set()
        alphabet = [chr(code) for code in range(ord('a'), ord('z') + 1)]
        indexes = {}
        i = 0
        for letter in key:
            if letter != ' ' and letter not in newkeySearch:
                newkey += letter
                newkeySearch.add(letter)
                indexes[letter] = i
                i += 1
                if len(newkey) == 26:
                    break
        decoded = ''
        for letter in message:
            if letter == ' ':
                decoded += ' '
            else:
                decoded += alphabet[indexes[letter]]
        return decoded
