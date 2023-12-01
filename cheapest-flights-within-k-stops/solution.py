class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf] * n
        prices[src] = 0

        for i in range(k + 1):
            next_prices = prices.copy()
            for s, d, p in flights:
                next_prices[d] = min(next_prices[d] , prices[s] + p)
            prices = next_prices
        return -1 if prices[dst] == inf else prices[dst]