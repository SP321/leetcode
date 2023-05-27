class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp={}
        def dfs(i):
            if i==n:
                return 0
            if i in dp:
                return dp[i]
            res=float(-inf)
            scoresum=0
            for j in range(i,min(i+3,n)):
                scoresum+=stoneValue[j]
                res=max(res,scoresum-dfs(j+1))
            dp[i]=res
            return res
        ans=dfs(0)
        if ans>0:
            return "Alice"
        elif ans<0:
            return "Bob"
        return "Tie"