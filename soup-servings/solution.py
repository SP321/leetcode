class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dfs(i,j):
            if i<=0 and j<=0:
                return 0.5
            if i<=0:
                return 1
            if j<=0:
                return 0
            val= (dfs(i-100,j)+dfs(i-75,j-25)+dfs(i-50,j-50)+dfs(i-25,j-75))/4
            return val
        return dfs(n,n) if n<5000 else 1
        
        