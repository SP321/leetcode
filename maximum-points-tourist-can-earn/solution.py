class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @cache
        def dp(i,day):
            if day==k:
                return 0
            ans=0
            ans=max(ans,dp(i,day+1)+stayScore[day][i])
            for j in range(n):
                ans=max(ans,dp(j,day+1)+travelScore[i][j])
            return ans
        return max(dp(i,0) for i in range(n))