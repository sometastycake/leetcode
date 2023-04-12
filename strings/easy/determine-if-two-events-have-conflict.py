# https://leetcode.com/problems/determine-if-two-events-have-conflict/

from typing import List


class Solution:

    def getMinutes(self, event: List[str]) -> List[int]:
        eventMinutes = []
        for time in event:
            t = time.split(':')
            hour = int(t[0])
            minute = int(t[1])
            eventMinutes.append(hour * 60 + minute)
        return eventMinutes

    def between(self, value: int, l: int, r: int) -> bool:
        return l <= value <= r

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        e1 = self.getMinutes(event1)
        e2 = self.getMinutes(event2)
        e1Begin = e1[0]
        e1End = e1[1]
        e2Begin = e2[0]
        e2End = e2[1]
        return (
            self.between(e1Begin, e2Begin, e2End) or
            self.between(e2Begin, e1Begin, e1End) or
            self.between(e2End, e1Begin, e1End) or
            self.between(e1End, e2Begin, e2End)
        )
