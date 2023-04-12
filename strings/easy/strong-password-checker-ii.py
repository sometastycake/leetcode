# https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        specialSymbols = '!@#$%^&*()-+'
        digits = 0
        lowercase = 0
        uppercase = 0
        specials = 0
        lastSymbol = ''
        for letter in password:
            if letter == lastSymbol:
                return False
            if letter.isdigit():
                digits += 1
            elif letter.isalpha():
                if letter.islower():
                    lowercase += 1
                else:
                    uppercase += 1
            elif not specials and letter in specialSymbols:
                specials += 1
            lastSymbol = letter
        return digits > 0 and lowercase > 0 and uppercase > 0 and specials > 0
