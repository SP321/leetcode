
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c=Counter(nums)
        a=list(c.keys())
        a.sort()
        s=set(a)
        dp=defaultdict(int)
        dp[1]=(c[1]+1)//2
        for x in a:
            if x!=1:
                dp[x]=max(1,dp[x])
                if c[x]>=2:
                    if x**2 in s:
                        dp[x**2]=max(dp[x**2],dp[x]+1)
        return max(dp.values())*2-1