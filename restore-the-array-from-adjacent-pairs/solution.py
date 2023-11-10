class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for u, v in adjacentPairs:
            g[u].add(v)
            g[v].add(u)

        start = next(node for node, neighbors in g.items() if len(neighbors) == 1)
        
        ans = []
        def dfs(node: int, visited: set):
            ans.append(node)
            visited.add(node)
            for neighbor in g[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        dfs(start, visited)
        return ans