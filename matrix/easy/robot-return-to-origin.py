# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        directions = {
            'U': (-1, 0),
            'R': (0, 1),
            'D': (1, 0),
            'L': (0, -1),
        }
        startI, startJ = 0, 0
        for direction in moves:
            i, j = directions[direction]
            startI += i
            startJ += j
        return startI == 0 and startJ == 0
