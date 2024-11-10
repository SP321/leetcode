MOD=10**9+7
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        c=Counter()
        dp=Counter()
        for x in nums:
            cnt=c[x-1]+c[x+1]+1
            dp[x]+=dp[x-1]+dp[x+1]+x*cnt
            c[x]+=cnt
        return sum(dp.values())%MOD