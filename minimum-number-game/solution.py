class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(0,n-1,2):
            ans.extend(nums[i:i+2][::-1])
        return ans