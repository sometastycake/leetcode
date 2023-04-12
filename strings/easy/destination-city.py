# https://leetcode.com/problems/destination-city/

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        for source, destination in paths:
            sources.add(source)
        for source, destination in paths:
            if destination not in sources:
                return destination
