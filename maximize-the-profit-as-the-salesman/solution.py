class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        dp = [0] * (n + 1)
        offer_idx = 0

        for i in range(n):
            dp[i + 1] = dp[i]

            while offer_idx < len(offers) and offers[offer_idx][1] <= i:
                start, end, gold = offers[offer_idx]
                dp[end + 1] = max(dp[end + 1], gold + dp[start])
                offer_idx += 1

        return dp[n]