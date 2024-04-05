class Solution:
    def makeGood(self, s: str) -> str:
        st=['']
        for x in s:
            if (st[-1].islower() and st[-1].upper()==x) or (st[-1].isupper() and st[-1].lower()==x):
                st.pop()
            else:
                st.append(x)
        return ''.join(st)