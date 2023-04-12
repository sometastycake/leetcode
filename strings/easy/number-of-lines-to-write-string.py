# https://leetcode.com/problems/number-of-lines-to-write-string/

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        currentWidth = 0
        rows = 0
        for letter in s:
            width = widths[ord(letter) - ord('a')]
            if currentWidth + width <= 100:
                currentWidth += width
                continue
            rows += 1
            currentWidth = width
        if currentWidth:
            rows += 1
        return [rows, currentWidth]
