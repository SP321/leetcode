class Prefix2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefix = self.build_prefix_2d()

    def build_prefix_2d(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        prefix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j] + self.matrix[i][j]
        return prefix

    def get_sum(self, x1, y1, x2, y2):
        return self.prefix[x2 + 1][y2 + 1] - self.prefix[x1][y2 + 1] - self.prefix[x2 + 1][y1] + self.prefix[x1][y1]

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        mat=[[0]*m for _ in range(n)]
        mat2=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='X':
                    mat[i][j]=1
                if grid[i][j]=='Y':
                    mat[i][j]=-1
                mat2[i][j]=abs(mat[i][j])
        a=Prefix2D(mat)
        b=Prefix2D(mat2)
        ans=0
        for i in range(n):
            for j in range(m):
                if b.get_sum(0,0,i,j)>0 and a.get_sum(0,0,i,j)==0:
                    ans+=1
        
        return ans