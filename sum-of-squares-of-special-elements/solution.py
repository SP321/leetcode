class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        return sum(nums[x]**2 for x in range(len(nums)) if n%(x+1)==0)