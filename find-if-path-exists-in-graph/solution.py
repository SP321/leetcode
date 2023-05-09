class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj={}
        for u,v in edges:
            if u not in adj:
                adj[u]=[]
            if v not in adj:
                adj[v]=[]
            adj[u].append(v)
            adj[v].append(u)
        seen=[False]*n
        def dfs(i):
            if i==destination:
                return True
            ans=False
            seen[i]=True
            for x in adj[i]:
                if not seen[x]:
                    ans=ans or dfs(x)
            return ans
        return dfs(source)

