# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

from typing import List


class Solution:

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word[0] != word[-1]:
                continue
            if word == word[::-1]:
                return word
        return ''
