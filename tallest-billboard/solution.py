class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for rod in rods:
            for diff, max_y in list(dp.items()):
                dp[diff + rod] = max(dp.get(diff + rod, 0), max_y)
                dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0), max_y + min(diff, rod))
        return dp[0]

        
