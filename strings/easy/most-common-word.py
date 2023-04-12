# https://leetcode.com/problems/most-common-word/

from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = Counter()
        current = ''
        result = ''
        amount = 0
        for letter in paragraph + ' ':
            if letter.isalpha():
                current += letter
            else:
                current = current.lower()
                if current and current not in banned:
                    counter[current] += 1
                    if counter[current] > amount:
                        amount = counter[current]
                        result = current
                current = ''
        return result
