class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x in set(nums) if nums.count(x)==2]