# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:

    def getDistance(self, pointer: str, letter: str) -> int:
        d1 = abs(ord(pointer) - ord(letter))
        d2 = abs(ord(pointer) - ord('a')) + abs(ord(letter) - ord('z')) + 1
        d3 = abs(ord(letter) - ord('a')) + abs(ord(pointer) - ord('z')) + 1
        return min([d1, d2, d3])

    def minTimeToType(self, word: str) -> int:
        result = 0
        pointer = 'a'
        for letter in word:
            if letter == pointer:
                result += 1
            else:
                result += self.getDistance(pointer, letter) + 1
                pointer = letter
        return result
