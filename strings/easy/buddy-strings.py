# https://leetcode.com/problems/buddy-strings/

from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        counterS = Counter(s)
        counterGoal = Counter(goal)
        if len(counterS) != len(counterGoal):
            return False
        for letter in counterS:
            if letter not in counterGoal:
                return False
        for letter in counterGoal:
            if letter not in counterS:
                return False
        for letter, amount in counterS.items():
            if amount != counterGoal[letter]:
                return False
        amount = 0
        uniqueLettersS = set()
        uniqueLettersGoal = set()
        for letterS, letterGoal in zip(s, goal):
            uniqueLettersS.add(letterS)
            uniqueLettersGoal.add(letterGoal)
            if letterS != letterGoal:
                amount += 1
                if amount > 2:
                    return False
        if amount == 0 and len(uniqueLettersS) == len(s) and len(uniqueLettersGoal) == len(goal):
            return False
        return True
