# https://leetcode.com/problems/flood-fill/

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        result = []
        rows = len(image)
        cols = len(image[0])
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(image[i][j])
            result.append(row)
        base_color = image[sr][sc]
        queue = [(sr, sc)]
        while queue:
            i, j = queue.pop()
            result[i][j] = color
            if i - 1 >= 0 and result[i - 1][j] == base_color:
                queue.append((i - 1, j))
            if j + 1 < cols and result[i][j + 1] == base_color:
                queue.append((i, j + 1))
            if i + 1 < rows and result[i + 1][j] == base_color:
                queue.append((i + 1, j))
            if j - 1 >= 0 and result[i][j - 1] == base_color:
                queue.append((i, j - 1))
        return result
