class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or k+maxPts<=n:
            return 1.0
        window=0
        for i in range(k,k+maxPts):
            window+=1 if i<=n else 0
        dp={}
        for i in range(k-1,-1,-1):
            dp[i]=window/maxPts
            rem=0
            if i+maxPts<=n:
                if i+maxPts not in dp:
                    dp[i+maxPts]=1
                rem=dp[i+maxPts]
            window+=dp[i]-rem
        return dp[0]