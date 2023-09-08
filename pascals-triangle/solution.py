class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @cache
        def pascal(row,col):
            if col==0 or col==row:
                return 1
            return pascal(row-1,col-1)+pascal(row-1,col)
        return [[pascal(row,col) for col in range(row+1)] for row in range(numRows)]