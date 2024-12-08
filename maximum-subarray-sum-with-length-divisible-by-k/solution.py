class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        nums=list(accumulate(nums))
        d={(-1)%k:0}
        n=len(nums)
        ans=-inf
        for i in range(n):
            if i%k in d:
                ans=max(ans,nums[i]-d[i%k])
                d[i%k]=min(d[i%k],nums[i])
            else:
                d[i%k]=nums[i]
        return ans