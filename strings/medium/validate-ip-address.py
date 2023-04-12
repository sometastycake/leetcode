# https://leetcode.com/problems/validate-ip-address/

class Solution:

    def checkIPv4(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part or not part.isdigit():
                return False
            if int(part) > 255:
                return False
            if len(part) > 1 and part.startswith('0'):
                return False
        return True

    def checkIPv6(self, ip: str) -> bool:
        parts = ip.split(':')
        p = {
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
            'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'
        }
        if len(parts) != 8:
            return False
        for part in parts:
            if not part or len(part) > 4:
                return False
            for c in part:
                if c not in p:
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.checkIPv4(queryIP):
            return 'IPv4'
        elif self.checkIPv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'
