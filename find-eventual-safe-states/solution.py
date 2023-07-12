class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * len(graph)
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            color[node] = GRAY
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            color[node] = BLACK
            return True
        return [node for node in range(len(graph)) if dfs(node)]