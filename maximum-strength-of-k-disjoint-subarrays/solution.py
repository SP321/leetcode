class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        dp0=[-inf]*k
        dp1=[-inf]*k
        for x in nums:
            dp_cur=[-inf]*k
            dp_cur[0]=max(dp0[0]+k*x,k*x)
            sign=1
            for i in range(1,k):
                sign=-sign
                dp_cur[i]=max(dp0[i]+(k-i)*x*sign,dp1[i-1]+(k-i)*x*sign)
            dp1=[max(a,b) for a,b in zip(dp1,dp_cur)]
            dp0=dp_cur
        print(dp1)
        return dp1[-1]