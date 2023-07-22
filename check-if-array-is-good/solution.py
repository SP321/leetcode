class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        return nums==list(range(1,nums[-1]+1))+[nums[-1]]