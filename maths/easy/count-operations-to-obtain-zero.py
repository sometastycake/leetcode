# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0
        while num1 and num2:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            result += 1
        return result
