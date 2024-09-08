class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        def check(mid):
            prev=-inf
            for x in sorted(start):
                cur = prev+mid
                if cur<x:
                    cur=x
                if cur>x+d:
                    return 1
                prev=cur
            return 0
        r=max(start)+d+1
        pos= bisect_right(range(r),0,key=check)
        return pos-1