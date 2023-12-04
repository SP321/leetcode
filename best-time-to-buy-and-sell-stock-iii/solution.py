class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)   
        @cache
        def dfs(i,b,s):
            if i==n:
                if b==s:
                    return 0
                return float("-inf")
            ans=dfs(i+1,b,s)
            if s>0:
                if b==s:
                    ans=max(ans,dfs(i+1,b-1,s)-prices[i])
                else:
                    ans=max(ans,dfs(i+1,b,s-1)+prices[i])
            return ans
        return dfs(0,2,2)
