class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        def sum_tl(i,j):
            s=set()
            i-=1
            j-=1
            while(i>=0 and j>=0):
                s.add(grid[i][j])
                i-=1
                j-=1
            return len(s)
            
        def sum_br(i,j):
            s=set()
            i+=1
            j+=1
            while(i<n and j<m):
                s.add(grid[i][j])
                i+=1
                j+=1
            return len(s)
        
        
        grid_ans=[[0]*m for i in range (n)]
        for i in range(n):
            for j in range(m):
                grid_ans[i][j]=abs(sum_tl(i,j)-sum_br(i,j))
        return grid_ans
                