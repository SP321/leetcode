class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp0=set()
        dp0.add(0)
        for x in rewardValues:
            dp1=set()
            for y in dp0:
                if y<x:
                    dp1.add(x+y)
            dp0=dp0|dp1
        return max(dp0)