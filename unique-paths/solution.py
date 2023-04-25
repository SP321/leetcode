class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=[[0]*m for i in range(n)]
        x[0][0]=1;
        for i in range(m):
            x[0][i]=1
        for i in range(n):
            x[i][0]=1
        for i in range(1,n):
            for j in range(1,m):
                x[i][j]=x[i-1][j]+x[i][j-1];
        return x[n-1][m-1]
        