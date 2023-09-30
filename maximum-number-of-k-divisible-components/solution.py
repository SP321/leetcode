class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        ans=0
        def dfs_sum(node, parent):
            nonlocal ans
            total = values[node]
            for child in graph[node]:
                if child != parent:
                    total += dfs_sum(child, node)
            if total%k==0:
                ans+=1
            return total
        
        dfs_sum(0, -1)
        return ans