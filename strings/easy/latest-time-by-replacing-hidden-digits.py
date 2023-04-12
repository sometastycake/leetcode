# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:

    def maximumTime(self, time: str) -> str:
        split = time.split(':')
        hour = split[0]
        minutes = split[1]
        if hour == '??':
            hour = '23'
        elif hour[1] == '?':
            if hour[0] in ('0', '1'):
                hour = hour[0] + '9'
            else:
                hour = '23'
        elif hour[0] == '?':
            if hour[1] in ('0', '1', '2', '3'):
                hour = '2' + hour[1]
            else:
                hour = '1' + hour[1]
        if minutes == '??':
            minutes = '59'
        elif minutes[1] == '?':
            minutes = minutes[0] + '9'
        elif minutes[0] == '?':
            minutes = '5' + minutes[1]
        return f'{hour}:{minutes}'
