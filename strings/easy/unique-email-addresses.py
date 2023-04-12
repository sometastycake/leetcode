# https://leetcode.com/problems/unique-email-addresses/

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            localName = ''
            index = email.index('@')
            for letter in email[:index]:
                if letter == '.':
                    continue
                if letter == '+':
                    break
                localName += letter
            localName += email[index:]
            result.add(localName)
        return len(result)
