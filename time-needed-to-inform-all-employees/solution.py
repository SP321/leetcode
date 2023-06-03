class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(node):
            ans = 0
            for child in graph[node]:
                ans = max(ans, dfs(child))
            return ans + informTime[node]

        return dfs(headID)