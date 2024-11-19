class Solution:
    def countSegments(self, s: str) -> int:
        ans=0
        for x in s.split():
            ans+=len(x)>0
        return ans