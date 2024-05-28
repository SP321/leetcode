class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        g=defaultdict(list)
        for x,y in richer:
            g[y].append(x) #neighbours are richer.
        @cache
        def dfs(x):
            ans=x
            for nei in g[x]:
                ans=min(ans,dfs(nei),key=lambda x:quiet[x])
            return ans
        return [dfs(i) for i in range(len(quiet))]