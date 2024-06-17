class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c=Counter(power)
        a=sorted(c.keys())
        n=len(a)
        @cache
        def dp(i):
            if i>=n:
                return 0
            j=i+1
            while j<n and a[j]<a[i]+3: # max 3 iterations
                j+=1
            return max(
                dp(i+1),
                dp(j)+a[i]*c[a[i]]
            )
        return dp(0)