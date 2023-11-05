class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(i,p):
            take=values[i] # take indicates delete(not add to score.)
            is_leaf=True
            leave=0
            for j in g[i]:
                if j!=p:
                    is_leaf=False
                    leave+=dfs(j,i)
            if is_leaf:
                return take
            return min(take,leave)
        
        return sum(values)-dfs(0,-1)