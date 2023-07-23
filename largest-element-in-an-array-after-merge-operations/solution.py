class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            if nums[i] > a:
                a = 0
            a += nums[i]
            ans = max(ans, a)
        return ans