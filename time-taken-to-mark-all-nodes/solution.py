class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        
        g = defaultdict(list)
        for u, v in edges:
            g[u].append( (v, 1 if v&1 else 2) )
            g[v].append( (u, 1 if u&1 else 2) )

        n = len(g)
        
        def dfs(u, p=-1):
            leaf_dist[u] = 0
            for v,w in g[u]:
                if v == p:
                    continue
                dfs(v, u)
                leaf_dist[u] = max(leaf_dist[u], leaf_dist[v] + w)

        def dfs2(u, p=-1):
            mx, smx = 0, 0
            for v,w in g[u]:
                if v == p:
                    continue
                cur=leaf_dist[v]+w
                if cur > mx:
                    mx, smx = cur, mx
                elif cur > smx:
                    smx = cur

            up = 1 if (u & 1) else 2
            for v,w in g[u]:
                if v == p:
                    continue
                if leaf_dist[v] + w == mx:
                    dist[v] = max(dist[v], max(dist[u] , smx ) + up ) 
                else:
                    dist[v] = max(dist[v], max(dist[u],  mx) + up )
                dfs2(v, u)

        leaf_dist, dist = [0] * n, [0] * n
        dfs(0)
        dfs2(0) # max dist other than subtree
        for i in range(n):
            dist[i] = max(dist[i], leaf_dist[i])
        return dist