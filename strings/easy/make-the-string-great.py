# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return s
        st = []
        for ch in s:
            if st:
                if ch.lower() == st[-1].lower() and (
                        ch.islower() and st[-1].isupper() or ch.isupper() and st[-1].islower()):
                    st.pop()
                    continue
            st.append(ch)
        return ''.join(st)
