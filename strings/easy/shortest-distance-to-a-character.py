# https://leetcode.com/problems/shortest-distance-to-a-character/

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        occurs = []
        for i, letter in enumerate(s):
            if letter == c:
                occurs.append(i)
        pointer = 0
        for i, letter in enumerate(s):
            if letter == c:
                answer.append(0)
                pointer += 1
                continue
            if pointer == 0:
                answer.append(occurs[pointer] - i)
            elif pointer < len(occurs):
                l = abs(i - occurs[pointer - 1])
                r = abs(i - occurs[pointer])
                if l < r:
                    answer.append(l)
                else:
                    answer.append(r)
            else:
                answer.append(abs(i - occurs[pointer - 1]))
        return answer
