class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        md = 10**9 + 7
        y = [i**x for i in range(1, n+1) if i**x<=n]
        @lru_cache(None)
        def dfs(i, target):
            if target == 0:
                return 1
            if target < 0 or i <0:
                return 0
            return (dfs(i - 1, target - y[i]) + dfs(i - 1, target))%md
        return dfs(len(y)-1,n)