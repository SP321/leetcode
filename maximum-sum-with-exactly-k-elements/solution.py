class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x=max(nums)
        return sum([i for i in range(x,x+k)])
        