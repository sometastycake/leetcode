# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        palindrome = s[0]
        i = 1
        j = 0
        while j < len(s):
            while i < len(s):
                if s[i] != s[j]:
                    i += 1
                else:
                    while self.isPalindrome(s[j: i + 1]) and i < len(s):
                        if len(s[j: i + 1]) > len(palindrome):
                            palindrome = s[j: i + 1]
                        i += 1
                    else:
                        i += 1
            if len(palindrome) >= len(s) // 2 + 1:
                return palindrome
            j += 1
            i = j + len(palindrome)
        return palindrome
