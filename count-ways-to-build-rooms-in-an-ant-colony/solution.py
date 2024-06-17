class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        g = defaultdict(list)
        for idx, v in enumerate(prevRoom):
            g[v].append(idx)
    
        def dfs(i):
            if i not in g:
                return (1, 1)
            ans = 0
            ways_i = 1
            for c in g[i]:
                ans_next, ways = dfs(c)
                ways_i = (ways_i * ways * comb(ans+ans_next, ans)) % (10**9 + 7)
                ans += ans_next
            return (ans + 1, ways_i)
        return dfs(0)[1]