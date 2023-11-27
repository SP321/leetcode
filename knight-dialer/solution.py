class Solution:
    def knightDialer(self, n: int) -> int:
        @cache
        def dfs(i,x,y):
            if x<0 or x>=3 or y<0 or y>=4:
                return 0
            if y==3 and x!=1:
                return 0
            if i==n-1:
                return 1
            ans=0
            for a,b in [[-1,-2],[-1,2],[1,-2],[1,2]]:
                ans+=dfs(i+1,x+a,y+b)
                ans+=dfs(i+1,x+b,y+a)
            return ans%(10**9+7)
        ans=0
        for i in range(3):
            for j in range(3):
                ans+=dfs(0,i,j)
        ans+=dfs(0,1,3)
        return ans%(10**9+7)