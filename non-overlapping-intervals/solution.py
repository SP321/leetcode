class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        cur_max=intervals[0][1]
        ans=0
        for i in range(1,n):
            if intervals[i][0]<cur_max:
                ans+=1
                cur_max=min(intervals[i][1],cur_max)
            else:
                cur_max=intervals[i][1]
        return ans
