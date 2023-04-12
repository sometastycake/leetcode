# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = 0
        minSalary = 2000000
        s = 0
        for value in salary:
            if value > maxSalary:
                maxSalary = value
            if value < minSalary:
                minSalary = value
            s += value
        s -= maxSalary
        s -= minSalary
        return round(s / (len(salary) - 2), 6)
