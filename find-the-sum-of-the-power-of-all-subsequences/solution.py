class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n=len(nums)
        @cache
        def dp(i,k):
            if i==n:
                return 1 if k==0 else 0
            ans=2*dp(i+1,k)
            if k>=nums[i]:
                ans+=dp(i+1,k-nums[i])
            return ans%int(1e9+7)
        return dp(0,k)