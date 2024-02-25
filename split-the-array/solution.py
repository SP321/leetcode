class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c=Counter(nums)
        return max(c.values())<=2