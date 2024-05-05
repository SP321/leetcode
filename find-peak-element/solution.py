class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return bisect_left(range(len(nums)-1),True,key=lambda k:nums[k+1]-nums[k]<0)