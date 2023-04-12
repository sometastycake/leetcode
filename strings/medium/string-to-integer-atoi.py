# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0
        minus = False
        if s[0] in ('-', '+'):
            if s[0] == '-':
                minus = True
            s = s[1:]
        if not s or not s[0].isdigit():
            return 0
        i = 0
        number = ''
        while i < len(s) and s[i].isdigit():
            number += s[i]
            i += 1
        number = int(number)
        if minus:
            number = -number
        if number < -2 ** 31:
            return -2 ** 31
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return number
