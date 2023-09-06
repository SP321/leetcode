class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        x = sum(i * num for i, num in enumerate(nums))
        ans = x
        s = sum(nums)

        for a in reversed(nums):
          x += s - len(nums) * a
          ans = max(ans, x)

        return ans