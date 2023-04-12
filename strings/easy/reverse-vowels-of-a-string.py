# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i = 0
        j = len(s) - 1
        while i < j:
            iVowels = s[i] in vowels
            if iVowels and s[j] in vowels:
                tmp = result[i]
                result[i] = result[j]
                result[j] = tmp
                i += 1
                j -= 1
            elif iVowels:
                j -= 1
            else:
                i += 1
        return ''.join(result)
