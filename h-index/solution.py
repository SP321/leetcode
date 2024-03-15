class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans=0
        n=len(citations)
        for x in citations:
            ans=max(ans,min(x,n))
            n-=1
        return ans