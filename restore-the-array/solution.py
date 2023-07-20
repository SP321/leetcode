class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            ways, num = 0, 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                ways = (ways + dfs(j + 1)) % mod
            return ways
        return dfs(0)