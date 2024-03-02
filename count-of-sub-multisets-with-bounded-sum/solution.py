class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        dp = [1] + [0] * 50000
        mod = 10 ** 9 + 7
        count = Counter(nums)
        for a,c in count.items():
            for i in range(r, max(r - a, 0), -1):
                v = sum(dp[i - a * k] for k in range(c))
                for j in range(i, 0, -a):
                    v -= dp[j] - dp[j - a * c]
                    dp[j] = (dp[j] + v) % mod
        return (count[0] + 1) * sum(dp[l:r + 1]) % mod