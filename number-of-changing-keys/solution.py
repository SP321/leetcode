class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        ans=0
        for i in groupby(s):
            ans+=1
        return ans-1