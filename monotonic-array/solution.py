class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(nums[i-1]<=nums[i] for i in range(1,len(nums))) or all(nums[i-1]>=nums[i] for i in range(1,len(nums))) 