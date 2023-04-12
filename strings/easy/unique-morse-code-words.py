# https://leetcode.com/problems/unique-morse-code-words/

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..'
        }
        result = set()
        for word in words:
            t = ''
            for letter in word:
                t += morse[letter]
            result.add(t)
        return len(result)
