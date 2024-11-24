class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append([v, w])
            g[v].append([u, w])

        def dfs(u, par = -1):
            ans = 0
            diff = []
            for v, w in g[u]:
                if v == par:
                    continue
                sm1, sm2 = dfs(v, u)
                ans += sm2
                diff.append(max(0, sm1 + w - sm2))
            diff.sort(reverse = True)
            return ans + sum(diff[:k - 1]), ans + sum(diff[:k])

        return dfs(0)[1]