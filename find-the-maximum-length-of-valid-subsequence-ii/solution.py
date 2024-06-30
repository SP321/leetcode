class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(i):
                x = (nums[i] + nums[j]) % k
                if x < 0:
                    x += k
                if dp[j][x] == 0:
                    dp[i][x] = 2
                else:
                    dp[i][x] = max(dp[i][x], dp[j][x] + 1)
                ans = max(ans, dp[i][x])
        return ans