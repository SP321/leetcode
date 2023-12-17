class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        s=set(range(1,(n**2)+1))
        repeated=None
        for row in grid:
            for val in row:
                if val not in s:
                    repeated=val
                s.discard(val)
        return [repeated,list(s)[0]]
            
            