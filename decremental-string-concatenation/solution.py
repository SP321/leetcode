class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n=len(words)
        dp=[[[-1]*26 for _ in range(26)] for _ in range(n)]
        def dfs(i,j,k):
            a=ord(j)-ord('a')
            b=ord(k)-ord('a')
            if i==n:
                return 0
            if dp[i][a][b]!=-1:
                return dp[i][a][b]
            left=dfs(i+1,words[i][0],k)
            if words[i][-1]==j:
                left-=1
            right=dfs(i+1,j,words[i][-1])
            if words[i][0]==k:
                right-=1
            dp[i][a][b] =len(words[i])+min(left,right)
            return dp[i][a][b]
        return len(words[0])+dfs(1,words[0][0],words[0][-1])  