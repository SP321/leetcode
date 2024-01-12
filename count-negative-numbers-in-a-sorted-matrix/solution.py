class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x=list(merge(*[i[::-1] for i in grid]))
        return bisect_right(x,-1)