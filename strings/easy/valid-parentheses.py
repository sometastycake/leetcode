# https://leetcode.com/problems/valid-parentheses

class Solution:

    def isOpenBracket(self, bracket: str) -> bool:
        return bracket in '([{'

    def isClosedBracket(self, bracket: str) -> bool:
        return bracket in ')]}'

    def bracketType(self, bracket: str) -> str:
        if bracket in '()':
            return 'circle'
        elif bracket in '[]':
            return 'square'
        else:
            return 'figure'

    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if self.isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                lastBracket = stack.pop()
                if self.isOpenBracket(lastBracket) and self.bracketType(bracket) != self.bracketType(lastBracket):
                    return False
        if stack:
            return False
        return True
