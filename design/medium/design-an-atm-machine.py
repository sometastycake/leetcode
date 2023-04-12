# https://leetcode.com/problems/design-an-atm-machine/

from typing import List


class ATM:

    def __init__(self):
        self.banknotes = {
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0,
        }

    def deposit(self, banknotesCount: List[int]) -> None:
        for banknote, amount in zip((20, 50, 100, 200, 500), banknotesCount):
            self.banknotes[banknote] += amount

    def withdraw(self, amount: int) -> List[int]:
        result = [0, 0, 0, 0, 0]
        i = 4
        for banknote in (500, 200, 100, 50, 20):
            if banknote > amount or self.banknotes[banknote] == 0:
                i -= 1
                continue
            banknotes = amount // banknote
            if banknotes > self.banknotes[banknote]:
                banknotes = self.banknotes[banknote]
            if banknotes:
                self.banknotes[banknote] -= banknotes
                amount -= banknotes * banknote
                result[i] = banknotes
            i -= 1
        if amount:
            self.deposit(result)
            return [-1]
        return result
