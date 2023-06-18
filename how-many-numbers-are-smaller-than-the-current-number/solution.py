class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2=sorted(nums)
        return [bisect.bisect_left(nums2,i) for i in nums]
