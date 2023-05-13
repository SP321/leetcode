class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        md = 10 ** 9 + 7
        ans = 0
        nums.sort()
        factor = 0
        for v in nums:
            square = v * v
            ans += square * factor + square * v
            ans %= md
            factor *= 2
            factor += v
            factor %= md
        return ans % md