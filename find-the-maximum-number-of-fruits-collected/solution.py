class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits)
        ans=0
        for i in range(n):
            ans+=fruits[i][i]
            fruits[i][i]=0
        @cache
        def dfs1(x,y):
            if x==n-1:
                if y==n-1:
                    return 0
                return -inf
            ans=-inf
            for ny in range(y-1,y+2):
                if 0<=ny<n:
                    ans=max(ans,dfs1(x+1,ny))
            return ans+fruits[x][y]

        @cache
        def dfs2(x,y):
            if y==n-1:
                if x==n-1:
                    return 0
                return -inf
            ans=-inf
            for nx in range(x-1,x+2):
                if 0<=nx<n:
                    ans=max(ans,dfs2(nx,y+1))
            return ans+fruits[x][y]

        ans+=dfs1(0,n-1)
        dfs1.cache_clear()
        ans+=dfs2(n-1,0)
        dfs2.cache_clear()
        return ans