class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        i=0
        j=c*r-1
        while i<=j:
            m=i+(j-i)//2
            x=matrix[m//c][m%c]
            if x<target:
                i=m+1
            elif x>target:
                j=m-1
            else:
                return True
        return False