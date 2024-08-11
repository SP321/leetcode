class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dp(i,mina):
            maxb=nums[i] if i==0 else nums[i-1]-mina
            if i==n:
                return 1
            ans=0
            for a in range(mina,nums[i]+1):
                b=nums[i]-a
                if b<=maxb:
                    ans+=dp(i+1,a)
            return ans%(10**9+7)
        return dp(0,0)