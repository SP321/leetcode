class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n=len(edges)+1
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u,p):
            s=set()
            c=1
            ans=0
            for v in g[u]:
                if v!=p:
                    c1,a=dfs(v,u)
                    ans+=a
                    c+=c1
                    s.add(c1)
            if len(s)<=1:
                ans+=1
            return c,ans
        return dfs(0,-1)[1]