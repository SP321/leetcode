class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n=len(nums)
        m=len(andValues)
        @cache
        def dp(i,j,cur=(1<<64)-1):
            if i==n:
                if j==m:
                    return 0
                return inf
            if j==m:
                return inf
            cur&=nums[i]
            ans=dp(i+1,j,cur)
            if cur==andValues[j]:
                ans=min(ans,dp(i+1,j+1)+nums[i])
            return ans
        ans=dp(0,0)
        return ans if ans!=inf else -1