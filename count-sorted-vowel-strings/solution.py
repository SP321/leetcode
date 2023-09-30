class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dfs(i,c):
            if c==0:
                return 0
            if i==n:
                return 1
            ans=0
            for j in range(c+1):
                ans+=dfs(i+1,j)
            return ans
        return dfs(0,5)
