class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0]+nums[1]<=nums[2]:
            return "none"
        return ["equilateral","isosceles","scalene"][len(set(nums))-1]