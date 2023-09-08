class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        @cache
        def dfs(i,target):
            if target==0:
                return 0
            if i==n or target<0:
                return float('inf')
            return min(
                dfs(i,target-coins[i])+1,
                dfs(i+1,target)
            )
        x=dfs(0,amount)
        return x if x!=float('inf') else -1