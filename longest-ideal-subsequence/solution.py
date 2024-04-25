class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=Counter()
        ans=0
        for c in s:
            i = ord(c)
            dp[i] = max(dp[j] for j in range(i - k,i + k + 1)) + 1
            ans=max(ans,dp[i])
        return ans