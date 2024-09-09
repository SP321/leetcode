class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([0]+[len(list(g[1])) for g in groupby(nums) if g[0]==1]) 