class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=max([matrix[k][j] for k in range(n)])
        return matrix