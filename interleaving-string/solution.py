class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s3)
        a=len(s1)
        b=len(s2)
        @cache
        def dfs(i,j,k):
            if i==a and j==b and k==n:
                return True
            if k==n:
                return False
            ans=False
            if i<a and s1[i]==s3[k]:
                ans=ans or dfs(i+1,j,k+1)
            if j<b and s2[j]==s3[k]:
                ans=ans or dfs(i,j+1,k+1)
            return ans
        return dfs(0,0,0)
            