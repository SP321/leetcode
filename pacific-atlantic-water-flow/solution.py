class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        def dfs(i,j,visited):
            visited.add((i,j))
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if (x,y)not in visited and\
                 x>=0 and x<n and\
                 y>=0 and y<m and\
                 heights[x][y]>=heights[i][j]:
                    dfs(x,y,visited)
        p=set()
        a=set()
        for i in range(n):
            if (i,0) not in p:
                dfs(i,0,p)
        for j in range(m):
            if (0,j) not in p:
                dfs(0,j,p)
        for i in range(n):
            if (i,m-1) not in a:
                dfs(i,m-1,a)
        for j in range(m):
            if (n-1,j) not in a:
                dfs(n-1,j,a)
        return list(p.intersection(a))
            