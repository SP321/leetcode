class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans=1
        n=len(nums)
        for i in range(2,n-1,2):
            if nums[i]+nums[i+1]==nums[i-1]+nums[i-2]:
                ans+=1
            else:
                break
        return ans