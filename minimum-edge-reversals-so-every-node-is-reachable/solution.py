class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(set)
        graph_a=defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph_a[v].add(u)
            graph_a[u].add(v)

        def dfs(i, prev):
            ans = 0
            for j in graph_a[i]:
                if j !=prev:
                    if j not in graph[i]:
                        ans += 1
                    ans += dfs(j, i)
            return ans

        def rotate_calc(i,prev):
            for j in graph_a[i]:
                if j!=prev:
                    if i in graph[j]:
                        ans[j]=ans[i]-1
                    else:
                        ans[j]=ans[i]+1
                    rotate_calc(j,i)
        
        ans = [0]*n
        ans[0]=dfs(0,-1)
        rotate_calc(0,-1)
        return ans