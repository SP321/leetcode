class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            pos=bisect_left(row,target)
            if pos<len(row) and row[pos]==target:
                return True
            if row[0]>target:
                return False
        return False