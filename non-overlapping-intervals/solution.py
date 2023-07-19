class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end_time = intervals[0][1]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end_time:
                ans += 1
            else:
                end_time = intervals[i][1]
        return ans