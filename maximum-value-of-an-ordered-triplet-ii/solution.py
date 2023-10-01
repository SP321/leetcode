class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        ma = list(accumulate(nums, max))
        ma_r = list(accumulate(nums[::-1], max))[::-1]
        ans=0
        for i in range(1,n-1):
            ans=max(ans,(ma[i-1]-(nums[i]))*ma_r[i+1])
        return ans