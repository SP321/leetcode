class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n=len(nums)
        @cache
        def dp(i,left,right):
            if i==n:
                return int(left!=0 and left==right)
            return (dp(i+1,left,right)+dp(i+1,gcd(nums[i],left),right)+dp(i+1,left,gcd(nums[i],right)))%(10**9+7)
        return dp(0,0,0)