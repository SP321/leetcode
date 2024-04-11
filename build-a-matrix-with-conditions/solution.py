class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def kahn(graph):
            n = len(graph)
            indeg, idx = [0] * n, [0] * n
            for i in range(n):
                for e in graph[i]:
                    indeg[e] += 1

            q, res = [], []
            for i in range(n):
                if indeg[i] == 0:
                    q.append(i)

            nr = 0
            while q:
                res.append(q.pop())
                idx[res[-1]], nr = nr, nr + 1
                for e in graph[res[-1]]:
                    indeg[e] -= 1
                    if indeg[e] == 0:
                        q.append(e)

            return res, idx, nr == n

        def prepareGraph(conditions, k):
            graph = [[] for _ in range(k)]
            for pre, post in conditions:
                graph[pre - 1].append(post - 1)
            return graph

        rowGraph = prepareGraph(rowConditions, k)
        colGraph = prepareGraph(colConditions, k)

        a, _, r_ok = kahn(rowGraph)
        _, b, c_ok = kahn(colGraph)

        if not r_ok or not c_ok:
            return []

        ans = [[0] * k for _ in range(k)]
        
        for r, x in enumerate(a):
            ans[r][b[x]] = x + 1

        return ans
