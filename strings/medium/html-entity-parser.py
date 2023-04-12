# https://leetcode.com/problems/html-entity-parser/

class Solution:
    def entityParser(self, text: str) -> str:
        m = {
            '&quot;': '"',
            '&apos;': "'",
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
        }
        i = 0
        result = ''
        while i < len(text):
            if text[i] != '&':
                result += text[i]
                i += 1
                continue
            c = '&'
            i += 1
            while i < len(text) and text[i] != '&':
                c += text[i]
                i += 1
                if c[-1] == ';':
                    break
            result += m.get(c, c)
        return result
