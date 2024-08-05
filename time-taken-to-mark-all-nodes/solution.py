class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append( (v,2-(v&1)))
            g[v].append( (u,2-(u&1)))
        n=len(edges)+1
        h=[0]*n
        def dfs(u,p):
            for v,w in g[u]:
                if v!=p:
                    dfs(v,u)
                    h[u]=max(h[u],h[v]+w)
        d=[0]*n
        def dfs2(u,p):
            mx,mx2=0,0
            up=2-(u&1)
            for v,w in g[u]:
                if v!=p:
                    down=2-(v&1)
                    dist=down+h[v]
                    if dist>mx:
                        mx,mx2=dist,mx
                    elif dist>mx2:
                        mx2=dist
            for v,w in g[u]:
                if v!=p:
                    down=2-(v&1)
                    dist=down+h[v]
                    if dist==mx:
                        d[v]=max(up+mx2,up+d[u])
                    else:
                        d[v]=max(up+mx,up+d[u])
                    dfs2(v,u)
        dfs(0,-1)
        dfs2(0,-1)
        for i in range(n):
            d[i]=max(d[i],h[i])
        return d