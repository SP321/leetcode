class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m=len(nums1)
        n=len(nums2)
        dp=[[-1]*n for _ in range(m)]
        def solve(i,j):
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            connect=0
            dp[i][j]=max(solve(i,j+1),solve(i+1,j))
            if nums1[i]==nums2[j]:
                dp[i][j]=max(dp[i][j],1+solve(i+1,j+1))
            return dp[i][j]
        return solve(0,0)