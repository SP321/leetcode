class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dp(i,j,k):
            if k<0:
                return 0
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            ans=0
            for dx,dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                ans+=dp(i+dx,j+dy,k-1)
            return ans%(1e9+7)
        return dp(startRow,startColumn,maxMove)