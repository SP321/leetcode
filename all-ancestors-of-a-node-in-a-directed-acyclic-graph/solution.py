class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans = {i: set() for i in range(n)}

        in_degree = defaultdict(int)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        queue = deque([node for node in range(n) if in_degree[node] == 0])
        top_order = []
        
        while queue:
            node = queue.popleft()
            top_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        for node in top_order:
            for nei in graph[node]:
                ans[nei].update(ans[node])
                ans[nei].add(node)
        
        return [sorted(ans[i]) for i in range(n)]