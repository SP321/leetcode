class Solution:
    def numberOfWays(self, corridor: str) -> int:
        x=[len(i)+1 for i in corridor.split("S")]
        if len(x)<3 or len(x)%2==0:
            return 0
        return prod(x[2:-2:2])%(10**9+7)