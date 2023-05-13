class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp=[0]*(high+1)
        dp[0]=1
        md=int(1e9+7)
        ans=0
        for i in range(high+1):
            if i+zero<=high:
                dp[i+zero]+=dp[i]
                dp[i+zero]%=md
            if i+one<=high:
                dp[i+one]+=dp[i]
                dp[i+one]%=md
            if i>=low:
                ans+=dp[i]
                ans%=md
        return ans