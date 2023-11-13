class Solution:
    def insert(self, intervals: List[List[int]], x: List[int]) -> List[List[int]]:
        i = bisect.bisect_left(intervals, x)
        ans = intervals[:i]
        
        if ans and x[0] <= ans[-1][1] :
            ans[-1][1] = max(ans[-1][1], x[1])
        else:
            ans.append(x)

        for i in range(i,len(intervals)):
            if intervals[i][0]<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                return ans+ intervals[i:]
        return ans