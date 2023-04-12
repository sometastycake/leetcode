# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = 0
        i = 0
        while i < len(word):
            j = i
            substr = set()
            while j < len(word) and word[j] in vowels:
                substr.add(word[j])
                if len(substr) >= 5:
                    result += 1
                j += 1
            i += 1
        return result
