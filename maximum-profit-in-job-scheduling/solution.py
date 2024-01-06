class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        x=list(map(list,zip(startTime,endTime,profit)))
        x.sort()

        n=len(x)
        @cache
        def dp(i):
            if i==n:
                return 0
            s,e,p=x[i]
            ans=dp(i+1)
            pos=bisect_left(x,[e,float("-inf"),float("-inf")])
            ans=max(ans,dp(pos)+p)
            return ans
        return dp(0)

            
