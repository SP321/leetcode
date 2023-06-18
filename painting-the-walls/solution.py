class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = {}
        @lru_cache(None)
        def dfs(i, total_time_needed):
            if total_time_needed<1:
                return 0
            if i == n:
                return float('inf')
            include = cost[i] + dfs(i + 1,total_time_needed-time[i]-1)
            exclude = dfs(i + 1, total_time_needed)
            return  min(include, exclude)
        return dfs(0, n)