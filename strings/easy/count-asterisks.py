# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        amount = 0
        pair = False
        for letter in s:
            if letter == '|' and not pair:
                pair = True
                if amount:
                    result += amount
                    amount = 0
            elif letter == '|' and pair:
                pair = False
            elif not pair and letter == '*':
                amount += 1
        if not pair and amount:
            result += amount
        return result
