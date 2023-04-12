# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = s
        i = 0
        while i + 1 < len(result):
            if result[i] == result[i + 1]:
                result = result[:i] + result[i + 2:]
                if i:
                    i -= 1
            else:
                i += 1
        return result
