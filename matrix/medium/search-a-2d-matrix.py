# https://leetcode.com/problems/search-a-2d-matrix/
# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


class Solution:

    def search(self, array: List[int], target: int) -> bool:
        i = 0
        j = len(array) - 1
        while i <= j:
            mid = (j + i) // 2
            if array[mid] == target:
                return True
            if array[mid] < target:
                i = mid + 1
                continue
            if array[mid] > target:
                j = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if array[0] > target:
                return False
            if array[0] <= target <= array[-1]:
                result = self.search(array, target)
                if result:
                    return True
        return False
