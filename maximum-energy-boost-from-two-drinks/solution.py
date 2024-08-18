class Solution:
    def maxEnergyBoost(self, A: List[int], B: List[int]) -> int:
        n=len(A)

        @cache
        def dp(i,is_a=True):
            if i>=n:
                return 0
            val= A[i] if is_a else B[i]
            ans=dp(i+1,is_a)+val
            ans=max(ans,val+dp(i+2,not is_a))
            return ans
        return max(dp(0,True),dp(0,False))