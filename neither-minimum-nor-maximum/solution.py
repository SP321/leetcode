class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        ma=max(nums)
        mi=min(nums)
        for i in nums:
            if i !=mi and i!=ma:
                return i
        return -1
        