class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        m = 2 * k + 1
        n = len(nums)
        ans = [-1] * n
        window_sum = 0
        for i in range(n):
            window_sum += nums[i]
            if i >= m:
                window_sum -= nums[i - m]
            if i >= m - 1:
                ans[i - k] = window_sum // m
        return ans