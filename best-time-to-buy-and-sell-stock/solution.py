class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin=prices[0]
        ans=0
        for i in prices:
            curmin=min(curmin,i)
            ans=max(ans,i-curmin)
        return ans