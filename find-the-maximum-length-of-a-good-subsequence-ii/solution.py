class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [defaultdict(int) for i in range(k + 1)]
        ans = [0] * (k + 1)
        for x in nums:
            for i in range(k, -1, -1):
                dp[i][x] = max(dp[i][x] + 1, ans[i - 1] + 1 if i else 0)
                ans[i] = max(ans[i], dp[i][x])
        return ans[k]