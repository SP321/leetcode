class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n < 2:
            return 0

        hold = [0] * n
        not_hold = [0] * n
        
        hold[0] = -prices[0] 
        not_hold[0] = 0 
        hold[1] = max( hold[0], -prices[1])
        not_hold[1] = max(0, prices[1] +hold[0])
        
        for i in range(2, n):
            hold[i] = max(hold[i - 1], not_hold[i - 2] - prices[i])
            not_hold[i] = max(not_hold[i - 1], hold[i - 1] + prices[i])
        
        return not_hold[n - 1]