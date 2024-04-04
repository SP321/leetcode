class Solution:
    def maxDepth(self, s: str) -> int:
        ct=0
        ans=0
        for x in s:
            if x =='(':
                    ct+=1
                    ans=max(ans,ct)
            elif x == ')':
                    ct-=1
        return ans