class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        a=[i+x for i,x in enumerate(values)]
        b=[-i+x for i,x in enumerate(values)]
        lmax=list(accumulate(a,lambda x,y:max(x,y)))
        rmax=list(accumulate(b[::-1],lambda x,y:max(x,y)))[::-1]
        ans=0
        for i in range(n-1):
            ans=max(ans,lmax[i]+rmax[i+1])
        return ans