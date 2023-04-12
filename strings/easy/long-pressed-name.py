# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        stack = []
        i = 0
        for letter in typed:
            if not stack or stack[-1] != letter or i < len(name) and name[i] == letter:
                stack.append(letter)
                i += 1
        return ''.join(stack) == name
