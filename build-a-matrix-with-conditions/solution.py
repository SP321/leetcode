class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0] * k for _ in range(k)]
		
        def topological(condition):
            graph = defaultdict(list)
            indegree = [0] * k
            for a, b in condition:
                graph[a].append(b)
                indegree[b - 1] += 1
            
            que = deque()
            for i, val in enumerate(indegree):
                if val == 0:
                    que.append(i + 1)
                    
            order = []
            
            while que:
                temp = que.popleft()
                order.append(temp)
                
                for child in graph[temp]:
                    indegree[child - 1] -= 1
                    if indegree[child - 1] == 0:
                        que.append(child)
                        
            return order
                        
        row_order = topological(rowConditions)
        col_order = topological(colConditions)
        
        if len(row_order) < k or len(col_order) < k:
            return []
        
        for row, val in enumerate(row_order):
            col = col_order.index(val)
            ans[row][col] = val
            
        return ans