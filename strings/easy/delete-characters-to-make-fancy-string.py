# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        result = ''
        substr = ''
        for letter in s:
            if not substr or substr[-1] == letter:
                substr += letter
            else:
                if len(substr) < 3:
                    result += substr
                else:
                    result += substr[:2]
                substr = letter
        if substr:
            if len(substr) < 3:
                result += substr
            else:
                result += substr[:2]
        return result
