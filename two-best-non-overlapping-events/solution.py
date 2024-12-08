class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n=len(events)
        mx=[0]
        for i in range(n-1,-1,-1):
            mx.append(max(events[i][2],mx[-1]))
        mx=mx[::-1]
        j=0
        ans=mx[0]
        for i in range(n):
            j=bisect_left(range(n),True,key=lambda k:events[k][0]>events[i][1],lo=1)
            if j<n:
                ans=max(ans,mx[j]+events[i][2])
        return ans