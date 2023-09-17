class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        ans = 0
        
        if nums[0] > 0:
            ans += 1
            
        for i in range(1, n):
            if nums[i] - nums[i-1] >= 2 and i<nums[i] and i>nums[i-1]:
                ans += 1

        if n>nums[-1] and len(nums)>0:
            ans+=1

        return ans