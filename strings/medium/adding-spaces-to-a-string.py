# https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ''
        pointer = 0
        for i in range(len(s)):
            if pointer >= len(spaces) or i != spaces[pointer]:
                result += s[i]
            else:
                result += f' {s[i]}'
                pointer += 1
        return result
