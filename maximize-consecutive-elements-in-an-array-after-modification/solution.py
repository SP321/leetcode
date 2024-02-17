class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp=defaultdict(int)
        for x in sorted(nums):
            dp[x] ,dp[x+1]= dp[x-1]+1, dp[x]+1
        return max(dp.values())
