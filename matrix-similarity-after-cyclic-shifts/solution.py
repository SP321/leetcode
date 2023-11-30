class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k%=len(mat[0])
        for i in range(len(mat)):
            row=mat[i]
            if i%2==0:
                for j in range(len(row)):
                    if row[j]!=row[(j+k)%len(row)]:
                        return False
            else:
                for j in range(len(row)):
                    if row[j]!=row[(j-k)%len(row)]:
                        return False
        return True
                