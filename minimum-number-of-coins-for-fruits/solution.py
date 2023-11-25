class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def dfs(i,free_pos):
            if i==n:
                return 0
            ans=prices[i]+dfs(i+1,max(free_pos,i+i+1))
            if i<=free_pos:
                ans=min(ans,dfs(i+1,free_pos))
            return ans
        return dfs(0,-1)
