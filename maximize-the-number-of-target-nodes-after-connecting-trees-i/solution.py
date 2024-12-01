class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n=len(edges1)+1
        m=len(edges2)+1
        g=[[] for _ in range(n+m)]
        for u,v in edges1:
            g[u].append(v)
            g[v].append(u)

        for u,v in edges2:
            u+=n
            v+=n
            g[u].append(v)
            g[v].append(u)
        
        @cache
        def dp(u,k,par=None):
            if k==0:
                return 0
            ans=1
            for v in g[u]:
                if v!=par:
                    ans+=dp(v,k-1,u)
            return ans

        a=[dp(i,k+1) for i in range(n)]
        b=max(dp(n+i,k) for i in range(m))
        ans=[]
        for x in a:
            ans.append(x+b)
            
        dp.cache_clear()
        return ans