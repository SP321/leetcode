class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for j in range(k + 1):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j]=1
                for p in range(i):
                    if nums[p] == nums[i]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                
                if j > 0:
                    for p in range(i):
                        if nums[p] != nums[i]:
                            dp[i][j] = max(dp[i][j], dp[p][j-1] + 1)

        mx = 0
        for i in range(n):
            for j in range(k + 1):
                mx = max(mx, dp[i][j])
        
        return mx
