class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ma=0;
        for i in range(len(mat))[::-1]:
            if (mat[i].count(1)>=mat[ma].count(1)):
                ma=i
        return [ma,mat[ma].count(1)]
                
        