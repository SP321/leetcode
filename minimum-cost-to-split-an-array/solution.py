class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i>=len(nums):
                return 0
            ans=inf
            sm=0
            c=Counter()
            for j in range(i,len(nums)):
                c[nums[j]]+=1
                if c[nums[j]]==2:
                    sm+=2
                elif c[nums[j]]>2:
                    sm+=1
                ans=min(ans,dp(j+1)+k+sm)
            return ans
        return dp(0)