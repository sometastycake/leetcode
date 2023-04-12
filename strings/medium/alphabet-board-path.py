# https://leetcode.com/problems/alphabet-board-path/

class Solution:

    def moveRow(self, startI: int, endI: int) -> str:
        if startI < endI:
            return 'D' * (endI - startI)
        return 'U' * (startI - endI)

    def moveColumn(self, startJ: int, endJ: int) -> str:
        if startJ < endJ:
            return 'R' * (endJ - startJ)
        return 'L' * (startJ - endJ)

    def alphabetBoardPath(self, target: str) -> str:
        p = {
            'a': (0, 0),
            'b': (0, 1),
            'c': (0, 2),
            'd': (0, 3),
            'e': (0, 4),
            'f': (1, 0),
            'g': (1, 1),
            'h': (1, 2),
            'i': (1, 3),
            'j': (1, 4),
            'k': (2, 0),
            'l': (2, 1),
            'm': (2, 2),
            'n': (2, 3),
            'o': (2, 4),
            'p': (3, 0),
            'q': (3, 1),
            'r': (3, 2),
            's': (3, 3),
            't': (3, 4),
            'u': (4, 0),
            'v': (4, 1),
            'w': (4, 2),
            'x': (4, 3),
            'y': (4, 4),
            'z': (5, 0)
        }
        pointer = 'a'
        path = ''
        for c in target:
            startI, startJ = p[pointer]
            endI, endJ = p[c]
            if c != pointer:
                if c != 'z':
                    if startI != endI:
                        path += self.moveRow(startI, endI)
                    if startJ != endJ:
                        path += self.moveColumn(startJ, endJ)
                else:
                    if startJ != endJ:
                        path += self.moveColumn(startJ, endJ)
                    if startI != endI:
                        path += self.moveRow(startI, endI)
            path += '!'
            pointer = c
        return path
