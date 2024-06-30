class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        d = {1:0, n: n-1}
        for x, y in restrictions:
            d[x] = y
        
        xs = sorted(d.keys())

        min_c1 = inf
        c1={} # contains intercepts in y=x+c1 lines.
        for x in xs:
            y=d[x]
            c1[x] = min(min_c1,y-x)
            min_c1 = c1[x]

        min_c2 = inf 
        c2={} # contains intercepts in y=-x+c2 lines.
        for x in xs[::-1]:
            y=d[x]
            c2[x] = min(y+x,min_c2)
            min_c2 = c2[x]

        def intersection(c1, c2 ,x2):
            x = (c2 - c1) / 2
            y = x + c1
            if x > x2: # intersection should be within x=x2
                x = x2
                y = x + c1
            return (x, y)

        ans = 0
        for x1,x2 in pairwise(xs):
            _, yy = intersection(c1[x1], c2[x2] , x2)
            ans = max(ans, floor(yy))
        return ans