class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp={}
        ans=0
        for x in sorted(set(nums),reverse=True):
            dp[x]=1
            if x*x in dp:
                dp[x]+=dp[x*x]
                if dp[x]>ans:
                    ans=dp[x]
        return ans if ans>=2 else -1
