class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a, b = 0, -prices[0]
        for i in prices:
            a = max(a, b + i - fee)
            b = max(b, a - i)
        return a