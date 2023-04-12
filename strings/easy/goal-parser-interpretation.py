# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        i = 0
        n = len(command)
        while i < n:
            if command[i] == 'G':
                s += 'G'
                i += 1
            elif command[i: i + 2] == '()':
                s += 'o'
                i += 2
            elif command[i: i + 4] == '(al)':
                s += 'al'
                i += 4
        return s
