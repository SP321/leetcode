class Solution:
    def numWaterBottles(self, n: int, m: int) -> int:
        ans=0
        e=0
        while n>0:
            ans+=n
            e+=n
            n,e=divmod(e,m)
        return ans