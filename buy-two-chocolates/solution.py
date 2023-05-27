class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        x=prices[0]+prices[1]
        if x<=money:
            return money-x
        return money