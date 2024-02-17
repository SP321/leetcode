class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for t in set([nums[0]+nums[1],nums[-1]+nums[-2],nums[0]+nums[-1]]):
            @cache
            def dp(i,j):
                if j-i+1<2:
                    return 0
                ans=0
                if nums[j]+nums[j-1]==t:
                    ans=max(ans,dp(i,j-2)+1)
                if nums[i]+nums[i+1]==t:
                    ans=max(ans,dp(i+2,j)+1)
                if nums[i]+nums[j]==t:
                    ans=max(ans,dp(i+1,j-1)+1)
                return ans
            ans=max(ans,dp(0,n-1))
        return ans