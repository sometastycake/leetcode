# https://leetcode.com/problems/partition-labels/

from collections import Counter
from typing import List


class Solution:
    def checkPartition(self, partition: str, counter: Counter) -> bool:
        for letter in partition:
            if counter[letter]:
                return False
        return True

    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        result = []
        partition = ''
        for letter in s:
            counter[letter] -= 1
            partition += letter
            if self.checkPartition(partition, counter):
                result.append(len(partition))
                partition = ''
        return result
