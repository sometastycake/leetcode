# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = 0
        for letter in number:
            if letter.isdigit():
                digits += 1
        result = ''
        group = ''
        for letter in number:
            if letter in (' ', '-'):
                continue
            group += letter
            digits -= 1
            amount = len(group)
            if amount == 3 and digits != 1:
                result += group
                group = ''
                if digits > 0:
                    result += '-'
            elif amount == 2 and digits in (0, 2):
                result += group
                group = ''
                if digits > 0:
                    result += '-'
        return result

