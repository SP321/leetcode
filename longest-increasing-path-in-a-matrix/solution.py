class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        @cache
        def dfs(i,j):
            ans=1
            dirs=[[1,0],[0,1],[-1,0],[0,-1]]
            for dx,dy in dirs:
                a=i+dx
                b=j+dy
                if a>=0 and a<n and b>=0 and b<m and matrix[a][b]>matrix[i][j]:
                    ans=max(ans,1+dfs(a,b))
            return ans
        ans=0
        for i in range(n):
            for j in range(m):
                ans=max(ans,dfs(i,j))
        return ans
               