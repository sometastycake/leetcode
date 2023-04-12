# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            ('M',  1000),
            ('CM', 900),
            ('D',  500),
            ('CD', 400),
            ('C',  100),
            ('XC', 90),
            ('L',  50),
            ('XL', 40),
            ('X',  10),
            ('IX', 9),
            ('V',  5),
            ('IV', 4),
            ('I',  1),
        ]
        i = 0
        result = ''
        while i < len(values):
            digit = values[i][0]
            value = values[i][1]
            if value > num:
                i += 1
            else:
                amount = num // value
                result += digit * amount
                num -= value * amount
        return result
