class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g=defaultdict(lambda :float('inf'))
        sources=set()
        targets=set()
        for u,v,w in zip(original,changed,cost):
            g[u,v]=min(g[u,v],w)
            sources.add(u)
            targets.add(v)

        for k in sources&targets:
            for i in sources:
                for j in targets:
                    g[i,j]=min(g[i,j],g[i,k]+g[k,j])
        

        n=len(source)
        m=len(target)

        @cache
        def dp(i):
            if i==n:
                return 0
            ans=float('inf')
            if source[i]==target[i]:
                ans=dp(i+1)
            for u in sources:
                if source.startswith(u, i):
                    for v in targets:
                        if g[u,v]!=float('inf') and target.startswith(v, i):
                            ans = min(ans, dp(i + len(u)) + g[u,v])
            return ans
        ans=dp(0)
        return ans if ans!=float("inf") else -1