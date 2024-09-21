class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        a0,a1,a2,a3 = a
        w,x,y,z = -inf,-inf,-inf,-inf
        for c in b:
            if a3*c+y > z:
                z = a3*c+y
            if a2*c+x > y:
                y = a2*c+x
            if a1*c+w > x:
                x = a1*c+w
            if a0*c > w:
                w = a0*c
        return z