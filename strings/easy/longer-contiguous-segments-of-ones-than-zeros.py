# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:

    def getSizeOfSegment(self, s: str, value: str) -> int:
        result = 0
        segment = ''
        for letter in s:
            if (not segment or segment[-1] == value) and letter == value:
                segment += letter
            else:
                if len(segment) > result:
                    result = len(segment)
                if letter == value:
                    segment = letter
                else:
                    segment = ''
        if segment and len(segment) > result:
            result = len(segment)
        return result

    def checkZeroOnes(self, s: str) -> bool:
        return self.getSizeOfSegment(s, '1') > self.getSizeOfSegment(s, '0')
