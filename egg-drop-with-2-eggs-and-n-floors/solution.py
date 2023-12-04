class Solution:
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dfs(n,eggs):
            if n==1:
                return 0
            if eggs==0:
                return float("inf")
            ans=float("inf")
            for i in range(1,n):
                ans= min(ans,max(dfs(i,eggs-1),dfs(n-i,eggs))+1)
            return ans
        return dfs(n+1,2)
