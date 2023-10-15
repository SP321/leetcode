class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        n = len(grid)
        m = len(grid[0])
        def get(x):
            return grid[x//m][x%m]
        def put(x,val):
            ans[x//m][x%m]*=val
            ans[x//m][x%m]%=mod

        ans=[[1 for _ in range(m)] for i in range(n)]
        x=1
        for i in range(n*m):
            put(i,x)
            x*=get(i)
            x%=mod
        x=1
        for i in range(n*m)[::-1]:
            put(i,x)
            x*=get(i)
            x%=mod
        return ans