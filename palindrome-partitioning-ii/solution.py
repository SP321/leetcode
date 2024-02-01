class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]: return 0
        n = len(s)
        def valid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        @cache
        def dfs(p):
            if p == n:
                return 0
            res = n
            for i in range(n - 1, p - 1, -1):
                if valid(p, i):
                    v = dfs(i + 1)
                    if v + 1 > res:
                        return res
                    res = 1 + v
            return res
        return dfs(0) - 1