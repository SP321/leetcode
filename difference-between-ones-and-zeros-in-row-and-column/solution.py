class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        a,b=[],[]
        for row in grid:
            a.append(sum(row)-(len(row)-sum(row)))

        for col in zip(*grid):
            b.append(sum(col)-(len(col)-sum(col)))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j]=a[i]+b[j]
        return grid
