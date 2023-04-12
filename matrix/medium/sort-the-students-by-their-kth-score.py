# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        result = []
        values = []
        for i in range(len(score)):
            values.append((i, score[i][k]))
        sortedValues = list(sorted(values, key=lambda v: v[1], reverse=True))
        for row, _ in sortedValues:
            result.append(score[row])
        return result
