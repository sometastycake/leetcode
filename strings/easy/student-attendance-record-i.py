# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        prevLateIndex = -1
        for i, c in enumerate(s):
            if c == 'A':
                absent += 1
                if absent == 2:
                    return False
                continue
            if c == 'L':
                if i - 1 != prevLateIndex:
                    prevLateIndex = i
                    late = 1
                else:
                    late += 1
                    prevLateIndex = i
                    if late == 3:
                        return False
        return True
