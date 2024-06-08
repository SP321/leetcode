class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for x in s:
            if st and x.isdigit():
                st.pop()
            else:
                st.append(x)
        return ''.join(st)
            