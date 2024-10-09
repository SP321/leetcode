class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for x in s:
            if st and st[-1]=='(' and x==')':
                st.pop()
            else:
                st.append(x)
        return len(st)