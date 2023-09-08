class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def solve(start,end):
            @cache
            def dp(i):
                if i>=end:
                    return 0
                return max(dp(i+1),dp(i+2)+nums[i])
            return dp(start)
        if len(nums)==1:
            return nums[0]
        return max(solve(1,n),solve(0,n-1))