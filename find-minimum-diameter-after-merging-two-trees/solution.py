class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        g=defaultdict(list)
        for x,y in edges1:
            g[x].append(y)
            g[y].append(x)
        g2=defaultdict(list)
        for x,y in edges2:
            g2[x].append(y)
            g2[y].append(x)
        
        def bfs(start, g):
            visited = {}
            queue = deque([(start, 0)])
            farthest_node = start
            max_dist = 0
            
            while queue:
                current, dist = queue.popleft()
                visited[current] = dist
                
                for neighbor in g[current]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))
                        if dist + 1 > max_dist:
                            max_dist = dist + 1
                            farthest_node = neighbor
            
            return farthest_node, max_dist
        
        def helper(g):
            a,_=bfs(0,g)
            b,d=bfs(a,g)
            return a,b,d
        
        a,b,d1=helper(g)
        c,d,d2=helper(g2)
        return max(d1,d2,d1-(d1//2)+d2-(d2//2)+1)