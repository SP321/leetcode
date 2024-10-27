MOD=10**9+7
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i,l,r):
            if i==n:
                return int(l!=0 and l==r)
            ans=dp(i+1,l,r)
            ans+=dp(i+1,gcd(nums[i],l),r)
            ans+=dp(i+1,l,gcd(nums[i],r))
            return ans
        return dp(0,0,0)%MOD