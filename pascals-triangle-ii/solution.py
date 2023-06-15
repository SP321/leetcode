class Solution:
    def getRow(self, rowIndex : int) -> List[int]:
        @lru_cache(None)
        def dfs(rowIndex ,i):
            if i<0 or i>rowIndex:
                return 0
            if rowIndex==0:
                return 1
            return dfs(rowIndex-1,i-1)+dfs(rowIndex-1,i)
        return [dfs(rowIndex,i) for i in range(rowIndex+1)]
