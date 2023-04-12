# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = coordinates[0]
        row = int(coordinates[1])
        colIndexes = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        colIndex = colIndexes[col]
        if row % 2 and not colIndex % 2 or not row % 2 and colIndex % 2:
            return True
        return False
