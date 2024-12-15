class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        events=[[-1,0]]+events
        ans=-1
        mx=0
        for x,y in pairwise(events):
            if y[-1]-x[-1]==mx:
                ans=min(ans,y[0])
            if y[-1]-x[-1]>mx:
                ans=y[0]
                mx=y[-1]-x[-1]
        return ans