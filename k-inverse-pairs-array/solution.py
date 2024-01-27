class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def dp(n, k):
            if k==0:
                return 1
            if k<0 or n<=0:
                return 0
            return (dp(n-1, k)+dp(n, k-1)-dp(n-1, k-n)+10**9+7)%(10**9+7)
        return dp(n, k)