class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return math.prod(max(dimensions,key=lambda x:(x[0]**2+x[1]**2,math.prod(x))))