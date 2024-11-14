class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(k):
            cnt=0
            for x in quantities:
                cnt+=(x+k-1)//k
            return -cnt
        return bisect_left(range(10**5+10),-n,key=check,lo=1)