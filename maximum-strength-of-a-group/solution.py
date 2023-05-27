class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')
        for i in range(1, 1 << n):
            product = 1
            for j in range(n):
                if (i & (1 << j)) != 0:
                    product *= nums[j]
            ans = max(ans, product)
        return ans