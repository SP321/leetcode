class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.a=defaultdict(int)
        self.b=defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cur=grid[i][j]
                for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                    xx,yy=i+dx,j+dy
                    if 0<=xx<len(grid) and 0<=yy<len(grid[i]):
                        self.a[cur]+=grid[xx][yy]
                for dx,dy in [[1,1],[-1,-1],[-1,1],[1,-1]]:
                    xx,yy=i+dx,j+dy
                    if 0<=xx<len(grid) and 0<=yy<len(grid[i]):
                        self.b[cur]+=grid[xx][yy]



    def adjacentSum(self, value: int) -> int:
        return self.a[value]

    def diagonalSum(self, value: int) -> int:
        return self.b[value]
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)