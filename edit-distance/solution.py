class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        @cache
        def dp(i,j):
            if j==m:
                return n-i
            if i==n:
                return m-j
            ans=dp(i+1,j)+1#delete
            if word1[i]==word2[j]:
                ans=min(ans,dp(i+1,j+1))#match
            ans=min(ans,dp(i+1,j+1)+1)#replace
            ans=min(ans,dp(i,j+1)+1)#add
            return ans
        return dp(0,0)