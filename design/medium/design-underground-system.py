# https://leetcode.com/problems/design-underground-system/

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.activeCustomers = {}
        self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.activeCustomers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.activeCustomers.pop(id)
        self.time[(startStation, stationName)].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.time[(startStation, endStation)]
        return round(sum(time) / len(time), 6)
