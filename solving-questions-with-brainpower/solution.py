class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        for i in range(n):
            a=min(i+questions[i][1]+1,n)
            dp[a]=max(dp[a],dp[i]+questions[i][0])
            dp[i+1]=max(dp[i+1],dp[i])
        return dp[n]