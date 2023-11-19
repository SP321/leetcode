class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(i if nums[i-1] > nums[i] else 0 for i in range(1,len(nums)))