# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
        positionX, positionY = 0, 0
        visited = set()
        visited.add((0, 0))
        for direction in path:
            offset = directions[direction]
            if direction in ('N', 'S'):
                positionY += offset
            else:
                positionX += offset
            key = (positionX, positionY)
            if key in visited:
                return True
            visited.add(key)
        return False
