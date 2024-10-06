class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for u,v in invocations:
            g[u].append(v)

        sus=set([k])
        def dfs(u):
            sus.add(u)
            for v in g[u]:
                if v not in sus:
                    dfs(v)

        dfs(k)

        def dfs2(u):
            vis.add(u)
            for v in g[u]:
                if v not in vis:
                    dfs2(v)
        vis=set()
        for i in range(n):
            if i not in vis and i not in sus:
                dfs2(i)
        for x in sus:
            if x in vis:
                return list(range(n))
        return list(vis)



        