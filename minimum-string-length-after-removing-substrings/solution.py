class Solution:
    def minLength(self, s: str) -> int:
        st=deque()
        for x in s:
            if st and x=='D' and st[-1]=='C':
                st.pop()
            elif st and x=='B' and st[-1]=='A':
                st.pop()
            else:
                st.append(x)
        return len(st)
            