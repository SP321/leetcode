class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        heap_window = []
        j = 0
        for q, i in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                l, r = intervals[j]
                heappush(heap_window, (r - l + 1, r))
                j += 1
            while heap_window and heap_window[0][1] < q:
                heappop(heap_window)
            ans[i] = heap_window[0][0] if heap_window else -1
        
        return ans