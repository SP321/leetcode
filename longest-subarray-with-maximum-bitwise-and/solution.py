class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx=max(nums)
        return max(len(list(g[1])) for g in groupby(nums) if g[0]==mx)
        
