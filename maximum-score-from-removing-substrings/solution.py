class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(a,x,y):
            ans=0
            st=[]
            for ch in s:
                if ch==a[1] and st and st[-1]==a[0]:
                    st.pop()
                    ans+=x
                else:
                    st.append(ch)
            st2=[]
            for ch in st:
                if ch==a[0] and st2 and st2[-1]==a[1]:
                    st2.pop()
                    ans+=y
                else:
                    st2.append(ch)
            return ans
        if x>y:
            return helper("ab",x,y)
        return helper("ba",y,x)