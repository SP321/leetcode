class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n,m=len(mat),len(mat[0])
        if n*m!=r*c:
            return mat
        x,y=0,-1
        ans=[[0]*c for i in range(r)]
        for i in range(n):
            for j in range(m):
                if y+1<c:
                    x,y=x,y+1
                else:
                    x,y=x+1,0
                ans[x][y]=mat[i][j]
        return ans
