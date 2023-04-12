# https://leetcode.com/problems/backspace-string-compare/

class Solution:

    def remove(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove(s) == self.remove(t)
