class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        c=sum(x for row in grid for x in row)
        options=[]
        for i in range(n-n//2):
            for j in range(m-m//2):
                if n%2==1 and m%2==1 and i==n//2 and j==m//2:
                    x=[grid[i][j]]
                elif n%2==1 and i==n//2:
                    x=[grid[i][j],grid[i][m-j-1]]
                elif m%2==1 and j==m//2:
                    x=[grid[i][j],grid[n-i-1][j]]
                else:
                    x=[grid[i][j],grid[n-i-1][j],grid[i][m-j-1],grid[n-i-1][m-j-1]]
                ct=Counter(x)
                options.append((ct[0],ct[1]))
        @cache
        def dp(i,rem=c%4):
            if i==len(options):
                if rem==0:
                    return 0
                return inf
            x,y=options[i]
            return min(dp(i+1,(rem+x)%4)+x,dp(i+1,(rem-y)%4)+y)
        return dp(0)