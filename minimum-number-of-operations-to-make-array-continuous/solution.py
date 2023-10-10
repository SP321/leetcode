class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        nums=list(set(nums))
        nums.sort()
        j=0
        ans=0
        for i in range(len(nums)):
            while j<len(nums) and nums[j]-nums[i]<=n-1:
                j+=1
            ans=max(ans,j-i)
        return n-ans