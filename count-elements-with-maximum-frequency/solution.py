class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        x=list(c.values())
        mx=max(x)
        return mx*x.count(mx)