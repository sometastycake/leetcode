# https://leetcode.com/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        multipliers = []
        if time[0] == '?' and time[1] == '?':
            multipliers.append(24)
        else:
            if time[0] == '?':
                if time[1] in ('0', '1', '2', '3'):
                    multipliers.append(3)
                else:
                    multipliers.append(2)
            if time[1] == '?':
                if time[0] == '2':
                    multipliers.append(4)
                elif time[0] in ('0', '1'):
                    multipliers.append(10)
        if time[3] == '?' and time[4] == '?':
            multipliers.append(60)
        else:
            if time[3] == '?':
                multipliers.append(6)
            if time[4] == '?':
                if time[3] in ('0', '1', '2', '3', '4', '5'):
                    multipliers.append(10)
        if not multipliers:
            return 1
        result = multipliers[0]
        for i in range(1, len(multipliers)):
            result *= multipliers[i]
        return result
