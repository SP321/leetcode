class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for i,j in pairwise(range(n)):
            g[i].append(j)
        ans=[]
       
        for u,v in queries:
            g[u].append(v)
            @cache
            def dfs(i):
                if i==n-1:
                    return 0
                ans=inf
                for v in g[i]:
                    ans=min(ans,dfs(v)+1)
                return ans
            ans.append(dfs(0))
        return ans