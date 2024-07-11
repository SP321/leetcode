class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for x in s:
            if x==')':
                cur=[]
                while st and st[-1]!='(':
                    cur.append(st.pop())
                if st:
                    st.pop()
                st.extend(cur)
            else:
                st.append(x)
        return ''.join(st)