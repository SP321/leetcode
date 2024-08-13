class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        x=list(range(n))
        dp=[0]*(n+1)
        for i in range(n):
            for j in range(i+1,n+1):
                if set(arr[i:j])==set(x[i:j]):
                    dp[j]=max(dp[j],dp[i]+1)
        return dp[n]