class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1,st2=[],[]
        for i in s:
            if i =='#':
                if st1:
                 st1.pop()
            else:
                st1.append(i)
        for i in t:
            if i =='#':
                if st2:
                    st2.pop()
            else:
                st2.append(i)
        return st1==st2