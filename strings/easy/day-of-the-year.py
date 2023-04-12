# https://leetcode.com/problems/day-of-the-year/

class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:date.find('-')])
        month = int(date[date.find('-') + 1: date.rfind('-')])
        day = int(date[date.rfind('-') + 1:])
        days = {
            1: 31,
            2: 29 if not year % 4 and year != 1900 else 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        result = 0
        for i in range(1, 13):
            if i >= month:
                break
            result += days[i]
        return result + day
