class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n=len(b)
        @cache
        def dp(i,j):
            if j==4:
                return 0
            if i==n:
                return -inf
            ans=dp(i+1,j)
            ans=max(ans,dp(i+1,j+1)+b[i]*a[j])
            return ans
        return dp(0,0)