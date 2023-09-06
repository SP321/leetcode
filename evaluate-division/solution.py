class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        n=len(equations)
        for i in range(n):
            u,v=equations[i]
            w=values[i]
            graph[u].append((v,w))
            graph[v].append((u,1/w))
            
        def dfs(i,target,visited):
            if i in visited:
                return float('-inf')
            visited.add(i)
            if i==target:
                return 1.0
            for j,w in graph[i]:
                x=dfs(j,target,visited)
                if x>0:
                    return x*w
            return float('-inf')
        
        ans=[]
        for u,v in queries:
            if u not in graph:
                x=-1
            else:
                x=dfs(u,v,set())
            ans.append(max(x,-1))
        return ans
            