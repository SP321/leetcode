class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        index={}
        for i in range(len(arr)):
            index[arr[i]]=i
        for i in range(n):
            for j in range(m):
                mat[i][j]=index[mat[i][j]]
        x=[]
        for i in range(n):
            ma=0
            for j in range(m):
                if mat[i][j]>ma:
                    ma=mat[i][j]
            x.append(ma)
                
        for j in range(m):
            ma=0
            for i in range(n):
                if mat[i][j]>ma:
                    ma=mat[i][j]
            x.append(ma)
        return min(x)