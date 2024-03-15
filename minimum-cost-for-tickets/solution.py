class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp=[0]*(days[-1]+1)
        p=0
        for day in range(1,days[-1]+1):
            if day==days[p]:
                p+=1
                dp[day]=min(
                    dp[max(0,day-1)]+costs[0],
                    dp[max(0,day-7)]+costs[1],
                    dp[max(0,day-30)]+costs[2]
                )
            else:
                dp[day]=dp[day-1]
        return dp[days[-1]]