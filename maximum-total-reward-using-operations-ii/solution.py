class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        dp0=0
        dp0|=1<<0
        for x in rewardValues: 
            dp1 =dp0 & ((1<<x)-1)
            dp1<<=x
            dp0|=dp1
        return dp0.bit_length()-1