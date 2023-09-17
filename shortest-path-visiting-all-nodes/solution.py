class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_mask = (1 << n) - 1

        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = set(queue)
        
        while queue:
            i, mask, dist = queue.popleft()

            if mask == target_mask:
                return dist

            for j in graph[i]:
                new_mask = mask | (1 << j)
                if (j, new_mask) not in visited:
                    visited.add((j, new_mask))
                    queue.append((j, new_mask, dist + 1))
        
        return -1