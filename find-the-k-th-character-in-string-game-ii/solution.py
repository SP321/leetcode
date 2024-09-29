class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        sz=1
        st=[]
        for x in operations:
            if sz>k:
                break
            sz*=2
            st.append(x)
        val=0
        while st:
            opr=st.pop()
            half=sz//2
            if k>half:
                val+=opr
                val%=26
                k-=half
            sz=half
        return chr(ord('a')+val)