class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n=len(events)
        @lru_cache(None)
        def dp(i, k):
            if i == n or k==0:
                return 0
            j = bisect.bisect(events, [events[i][1], math.inf, math.inf], i + 1)
            return max(dp(i + 1, k), events[i][2] + dp(j, k - 1))
        return dp(0, k)
  