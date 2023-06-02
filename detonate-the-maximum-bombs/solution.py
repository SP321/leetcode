class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = math.dist([x1, y1], [x2, y2])
                if dist <= r1:
                    graph[i].append(j)
                if dist <= r2:
                    graph[j].append(i)
        def dfs(i):
            visited[i] = True
            size = 1
            for j in graph[i]:
                if not visited[j]:
                    size += dfs(j)
            return size
        ans = 0
        for i in range(n):
            visited = [False] * n
            ans = max(ans, dfs(i))
        return ans