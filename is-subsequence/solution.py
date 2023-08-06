class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def dfs(i,j):
            if i==len(s):
                return True
            if j==len(t):
                return False
            ans=dfs(i,j+1)
            if s[i]==t[j]:
                ans=ans or dfs(i+1,j+1)
            return ans
        return dfs(0,0)
                
                