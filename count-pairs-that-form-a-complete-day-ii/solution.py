class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d=Counter()
        ans=0
        for x in hours:
            x%=24
            need=24-x
            need%=24
            ans+=d[need]
            d[x]+=1
        return ans