class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix),len(matrix[0])
        flag_i0=any( matrix[i][0]==0 for i in range(n))
        flag_j0=any( matrix[0][j]==0 for j in range(m))
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        for i in range(n):
            if flag_i0:
                matrix[i][0]=0

        for j in range(m):
            if flag_j0:
                matrix[0][j]=0
                