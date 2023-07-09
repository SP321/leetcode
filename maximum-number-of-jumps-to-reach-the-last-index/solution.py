class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n=len(nums)
        graph=defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[j]-nums[i])<=target:
                    graph[i].append(j)
        dp=[-1]*(n+1)
        dp[0]=0
        for i in range(n):
            for j in graph[i]:
                if dp[i]>=0:
                    dp[j]=max(dp[j],dp[i]+1)
        return dp[n-1]