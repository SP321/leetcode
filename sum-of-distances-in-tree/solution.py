class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        ans = [0] * n
        count = [1] * n
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(root, p):
            for i in g[root]:
                if i != p:
                    dfs(i, root)
                    count[root] += count[i]
                    ans[root] += ans[i] + count[i]

        def dfs2(root, p):
            for i in g[root]:
                if i != p:
                    ans[i] = ans[root] - count[i] + n - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return ans