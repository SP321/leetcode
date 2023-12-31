class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(x%2==0 for x in nums)>=2