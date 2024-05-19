class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dp(pos,jump)->int:
            if pos>k+1:
                return 0
            ans=int(pos==k)+int(pos-1==k)
            ans+=dp(pos-1+(1<<jump),jump+1)
            ans+=dp(pos+(1<<jump),jump+1)
            return ans
        return dp(1,0)