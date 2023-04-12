# https://leetcode.com/problems/string-compression/

from typing import List


class Solution:

    def digits(self, n: int) -> List[str]:
        return list(str(n))

    def compress(self, chars: List[str]) -> int:
        answer = []
        i = 0
        while i < len(chars):
            char = chars[i]
            j = i
            while j < len(chars) - 1 and chars[j] == chars[j + 1]:
                j += 1
            c = j - i + 1
            answer.append(char)
            if c != 1:
                answer += self.digits(c)
            i = j + 1
        for i in range(len(answer)):
            chars[i] = answer[i]
        return len(answer)
