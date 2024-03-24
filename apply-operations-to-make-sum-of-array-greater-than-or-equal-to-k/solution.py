class Solution:
    def minOperations(self, k: int) -> int:
        @cache
        def dp(i):
            if(i>=k):
                return 0
            return min(dp(i+1)+1,((k-i+(i-1))//i))
        return dp(1)