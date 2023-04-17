class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        x=1
        for i in range(len(nums)):
            ans[i]*=x
            x*=nums[i]
        x=1
        for i in range(len(nums))[::-1]:
            ans[i]*=x
            x*=nums[i]
        return ans