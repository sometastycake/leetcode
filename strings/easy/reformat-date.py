# https://leetcode.com/problems/reformat-date/

class Solution:

    def toInt(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            result += s[i]
        if int(result) < 10:
            return '0' + result
        return result

    def reformatDate(self, date: str) -> str:
        months = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12',
        }
        day = self.toInt(date)
        month = months[date[date.find(' ') + 1: date.rfind(' ')]]
        year = date[date.rfind(' ') + 1:]
        return f'{year}-{month}-{day}'
