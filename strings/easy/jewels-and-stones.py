# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for jew in jewels:
            result += stones.count(jew)
        return result
