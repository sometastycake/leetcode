# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ''
        for ch in address:
            if ch == '.':
                s += '[.]'
            else:
                s += ch
        return s
