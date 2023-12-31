class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x=sorted(list(set(nums)))
        return x[-3] if len(x)>=3 else x[-1]