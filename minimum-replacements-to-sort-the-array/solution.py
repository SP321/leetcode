class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        ma = nums[-1]

        for num in reversed(nums[:-1]):
            c = (num + ma - 1) // ma
            ans += c - 1
            ma = num // c
            
        return ans