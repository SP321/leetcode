class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        lst = list(zip(*mat))
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(lst[j]) == 1:
                    res += 1
        return res