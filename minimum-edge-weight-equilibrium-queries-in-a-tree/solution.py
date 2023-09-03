class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        bin_max=int(math.log2(n)+1)
        up = [[-1] * bin_max for i in range(n)]
        prefix = {0:Counter()}  
        graph = defaultdict(list)
        depth = [0] * n
        for i, j, k in edges:
            graph[i].append((j, k))
            graph[j].append((i, k))


        def dfs(i, p, d):
            depth[i] = d
            for j in range(1, bin_max):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]

            for j, w in graph[i]:
                if j != p:
                    up[j][0]=i
                    prefix[j] = prefix[i]+Counter([w])
                    dfs(j, i, d + 1)
        dfs(0,-1,0)
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            for i in range(bin_max):
                if d & (1 << i):
                    u = up[u][i]
            if u == v:
                return u
            for i in range(bin_max-1, -1, -1):
                if up[u][i] != up[v][i]:
                    u, v = up[u][i], up[v][i]
            return up[u][0]
        
        ans = []
        
        for x, y in queries:
            l = lca(x, y)
            pre = prefix[x] + prefix[y] -  prefix[l] - prefix[l]
            pre=pre.values()
            a=0
            if len(pre)>0:
                a=sum(pre)-max(pre)
            ans.append(a)
        return ans