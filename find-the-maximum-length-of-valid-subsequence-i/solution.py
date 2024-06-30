class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        @cache
        def dp(i,prev=None,parity=0):
            if i==len(nums):
                return 0
            ans=dp(i+1,prev,parity)
            if prev==None or (prev+nums[i])%2==parity:
                ans=max(ans,dp(i+1,nums[i]%2,parity)+1)
            return ans

        return max(dp(0,None,1),dp(0,None,0))