class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        power_of_5 = [bin(5**i)[2:] for i in range(8)]
        n = len(s)
        @lru_cache(None)
        def dfs(i,prefix):
            if i==n:
                if prefix=="":
                    return 0
                else:
                    return float('inf')
            prefix+=s[i]
            if prefix in power_of_5:
                return min(1+dfs(i+1,""),dfs(i+1,prefix))
            else:
                return dfs(i+1,prefix)
        x=dfs(0,"")
        return x if x!=float("inf")else -1