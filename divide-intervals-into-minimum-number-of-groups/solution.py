class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        h=[]
        ans=1
        for start,end in sorted(intervals):
            heappush(h,end)
            while h and h[0]<start:
                heappop(h)
            ans=max(ans,len(h))
        return ans