# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        array = list(s)
        i = 0
        j = len(array) - 1
        while i < j:
            if not array[i].isalpha():
                i += 1
                continue
            if not array[j].isalpha():
                j -= 1
                continue
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i += 1
            j -= 1
        return ''.join(array)
