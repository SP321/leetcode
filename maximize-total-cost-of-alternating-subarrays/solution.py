class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache
        def dp(i,sign):
            if i==len(nums):
                return 0
            cur=nums[i]
            if sign==-1:
                cur=-cur
            return max(dp(i+1,-sign)+cur, dp(i+1,-1)+nums[i])
        return dp(0,1)